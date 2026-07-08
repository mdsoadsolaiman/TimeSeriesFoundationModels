"""Data loading utilities for the Bitcoin EDA pipeline."""

from pathlib import Path

import pandas as pd


def load_bitcoin_data(path):
    """Load raw Bitcoin minute-level data from a CSV file.

    Parameters
    ----------
    path : str or pathlib.Path
        Path to a CSV file with a Unix-seconds ``Timestamp`` column.

    Returns
    -------
    pandas.DataFrame
        Data sorted by timestamp with ``Timestamp`` converted to datetime.
    """
    csv_path = Path(path)
    df = pd.read_csv(csv_path)

    if "Timestamp" not in df.columns:
        raise ValueError("Expected a 'Timestamp' column in the Bitcoin CSV.")

    df["Timestamp"] = pd.to_datetime(df["Timestamp"], unit="s", utc=True)
    return df.sort_values("Timestamp").reset_index(drop=True)

