"""Preprocessing utilities for the Bitcoin EDA pipeline."""

import pandas as pd


def prepare_daily_bitcoin_data(df):
    """Convert minute-level Bitcoin data into daily OHLCV data.

    Parameters
    ----------
    df : pandas.DataFrame
        Raw Bitcoin data with ``Timestamp``, ``Open``, ``High``, ``Low``,
        ``Close``, and ``Volume`` columns.

    Returns
    -------
    pandas.DataFrame
        Daily data indexed by timestamp with OHLC prices and total volume.
    """
    required_columns = {"Timestamp", "Open", "High", "Low", "Close", "Volume"}
    missing_columns = required_columns.difference(df.columns)
    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"Missing required Bitcoin columns: {missing}")

    daily = df.copy()
    if pd.api.types.is_numeric_dtype(daily["Timestamp"]):
        daily["Timestamp"] = pd.to_datetime(daily["Timestamp"], unit="s", utc=True)
    else:
        daily["Timestamp"] = pd.to_datetime(daily["Timestamp"], utc=True)
    daily = daily.sort_values("Timestamp").set_index("Timestamp")

    daily = daily.resample("D").agg(
        {
            "Open": "first",
            "High": "max",
            "Low": "min",
            "Close": "last",
            "Volume": "sum",
        }
    )

    return daily.dropna(subset=["Open", "High", "Low", "Close"])
