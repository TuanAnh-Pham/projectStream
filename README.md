# Quant Streaming Risk Platform

A draft data engineering project that uses public APIs and Spark Structured Streaming to build real-time quantitative market-risk features. The project is designed to showcase skills relevant to quant data engineering roles: event-time processing, time-series normalization, rolling feature generation, data quality, and lakehouse-style data modeling.

## Project goal

Ingest market, crypto, macro, and news data from public APIs, process the feeds through a Bronze/Silver/Gold streaming architecture, and produce a feature table that can power dashboards, alerts, research notebooks, or lightweight backtests.

## Proposed architecture

```text
Public APIs
  ├── CoinGecko crypto prices
  ├── Alpha Vantage or Finnhub market data
  ├── FRED macro indicators
  └── NewsAPI/GDELT/Finnhub news events
        ↓
Python API producers
        ↓
Kafka or Redpanda topics
        ↓
Spark Structured Streaming
        ↓
Bronze raw Delta tables
        ↓
Silver normalized time-series tables
        ↓
Gold quant feature and risk tables
        ↓
Streamlit dashboard / FastAPI / notebooks
```

## API keys and secrets

API keys are intentionally kept out of source files. Copy `.env.example` to `.env` and fill in keys locally when you are ready to run API-backed jobs.

```bash
cp .env.example .env
```

Supported environment variables include:

- `ALPHA_VANTAGE_API_KEY`
- `FINNHUB_API_KEY`
- `NEWSAPI_API_KEY`
- `FRED_API_KEY`
- `KAFKA_BOOTSTRAP_SERVERS`

CoinGecko's simple price endpoint can be used for an initial no-key crypto demo.

## Current draft contents

```text
configs/                    Asset and topic configuration drafts
ingestion/common/            Shared settings and canonical event helpers
ingestion/producers/         Public API polling drafts
streaming/gold/              Spark Structured Streaming feature job draft
TODO.md                      Showcase checklist and project roadmap
.env.example                 Local-only API key template
requirements.txt             Python dependency starter list
```

## Example event schema

```json
{
  "event_type": "market_price",
  "symbol": "BTC",
  "asset_class": "crypto",
  "price": 65000.0,
  "source": "coingecko",
  "event_time": "2026-07-08T12:00:00+00:00",
  "ingest_time": "2026-07-08T12:00:01+00:00",
  "raw": {
    "usd": 65000.0
  }
}
```

## Quant features to implement

The Gold layer should produce features such as:

- Rolling 1-minute, 5-minute, and 15-minute returns
- Realized volatility
- Rolling high/low ranges
- VWAP where volume is available
- Return z-scores
- Cross-asset rolling correlations
- News-event counts and sentiment scores
- Macro regime flags
- Composite risk score by symbol

## Local setup draft

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the no-key CoinGecko producer draft:

```bash
python -m ingestion.producers.coingecko_producer
```

The producer currently prints canonical events to stdout. A later milestone should publish the events to Kafka or Redpanda.

## Resume framing

> Built a Spark Structured Streaming pipeline for public market, crypto, macroeconomic, and news data. Designed Bronze/Silver/Gold Delta tables, implemented event-time processing with watermarks and sliding windows, and generated rolling quantitative risk features including volatility, high/low ranges, correlations, and composite risk scores for dashboard and research use cases.

## Showcase roadmap

See [`TODO.md`](TODO.md) for a checklist of items to complete before using the project in interviews or portfolio demos.
