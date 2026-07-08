"""Draft Spark Structured Streaming job for rolling quant risk features."""
from __future__ import annotations

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, max as spark_max, min as spark_min, stddev, window


def build_asset_risk_features(prices):
    """Compute sliding-window features from normalized price events."""
    return (
        prices.withWatermark("event_time", "10 minutes")
        .groupBy(window(col("event_time"), "15 minutes", "1 minute"), col("symbol"), col("asset_class"))
        .agg(
            avg("price").alias("avg_price_15m"),
            stddev("price").alias("price_volatility_15m"),
            spark_min("price").alias("low_15m"),
            spark_max("price").alias("high_15m"),
        )
        .select(
            col("symbol"),
            col("asset_class"),
            col("window.start").alias("window_start"),
            col("window.end").alias("window_end"),
            col("avg_price_15m"),
            col("price_volatility_15m"),
            col("low_15m"),
            col("high_15m"),
        )
    )


def main() -> None:
    spark = SparkSession.builder.appName("quant-risk-features").getOrCreate()
    prices = spark.readStream.format("delta").load("data/silver/market_prices")
    features = build_asset_risk_features(prices)
    (
        features.writeStream.format("delta")
        .option("checkpointLocation", "data/checkpoints/gold_asset_risk_features")
        .outputMode("append")
        .start("data/gold/asset_risk_features")
        .awaitTermination()
    )


if __name__ == "__main__":
    main()
