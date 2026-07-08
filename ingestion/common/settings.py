"""Environment-driven settings for local producers and streaming jobs."""
from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class Settings:
    kafka_bootstrap_servers: str = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
    coingecko_base_url: str = os.getenv("COINGECKO_BASE_URL", "https://api.coingecko.com/api/v3")
    alpha_vantage_api_key: str | None = os.getenv("ALPHA_VANTAGE_API_KEY")
    fred_api_key: str | None = os.getenv("FRED_API_KEY")
    finnhub_api_key: str | None = os.getenv("FINNHUB_API_KEY")
    newsapi_api_key: str | None = os.getenv("NEWSAPI_API_KEY")
