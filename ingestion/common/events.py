"""Canonical event helpers used by API pollers."""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def market_price_event(symbol: str, asset_class: str, price: float, source: str, raw: dict[str, Any]) -> dict[str, Any]:
    return {
        "event_type": "market_price",
        "symbol": symbol,
        "asset_class": asset_class,
        "price": price,
        "source": source,
        "event_time": utc_now_iso(),
        "ingest_time": utc_now_iso(),
        "raw": raw,
    }
