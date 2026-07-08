# Showcase TODO List

## Must-have demo items
- [ ] Add real API keys to a local `.env` copied from `.env.example`.
- [ ] Wire producers to Kafka or Redpanda instead of stdout.
- [ ] Build Bronze streaming ingestion from Kafka into Delta tables.
- [ ] Build Silver normalization with timestamp parsing, symbol mapping, and duplicate removal.
- [ ] Expand Gold features to include returns, realized volatility, VWAP, z-scores, and rolling correlation.
- [ ] Create a Streamlit dashboard with latest prices, volatility, risk scores, and data-quality metrics.
- [ ] Add screenshots or a short demo GIF to the README.

## Quant-focused enhancements
- [ ] Add FRED macro indicators such as FEDFUNDS, DGS2, DGS10, and CPIAUCSL.
- [ ] Create a macro regime classifier: risk-on, neutral, or risk-off.
- [ ] Add news/event counts and sentiment fields from NewsAPI, GDELT, or Finnhub.
- [ ] Produce a simple composite risk score by symbol and window.
- [ ] Add a backtesting notebook that consumes Gold feature tables.

## Engineering polish
- [ ] Add unit tests for feature calculations with small Spark DataFrames.
- [ ] Add API contract tests using mocked API responses.
- [ ] Add Great Expectations or custom data quality checks.
- [ ] Add Docker Compose for Spark, Kafka/Redpanda, and dashboard services.
- [ ] Add orchestration with Airflow, Dagster, or Prefect.
- [ ] Document data lineage from raw API payload to Gold features.
