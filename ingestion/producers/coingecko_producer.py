"""Poll CoinGecko prices and emit canonical JSON events.

This draft prints events to stdout so the project works before Kafka is wired in.
Replace `print(event)` with a Kafka producer send in the production milestone.
"""
from __future__ import annotations

import time
from typing import Iterable

import requests

from ingestion.common.events import market_price_event
from ingestion.common.settings import Settings


DEFAULT_ASSETS = {"bitcoin": "BTC", "ethereum": "ETH", "solana": "SOL"}


def fetch_prices(settings: Settings, asset_ids: Iterable[str]) -> dict:
    ids = ",".join(asset_ids)
    response = requests.get(
        f"{settings.coingecko_base_url}/simple/price",
        params={"ids": ids, "vs_currencies": "usd"},
        timeout=15,
    )
    response.raise_for_status()
    return response.json()


def run_once(settings: Settings = Settings()) -> list[dict]:
    payload = fetch_prices(settings, DEFAULT_ASSETS.keys())
    events = []
    for asset_id, symbol in DEFAULT_ASSETS.items():
        price = float(payload[asset_id]["usd"])
        events.append(market_price_event(symbol, "crypto", price, "coingecko", payload[asset_id]))
    return events


if __name__ == "__main__":
    while True:
        for event in run_once():
            print(event, flush=True)
        time.sleep(30)
