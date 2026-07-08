# TimeSeriesFoundationModels

This project investigates trustworthy foundation models for time-series forecasting.

The aim is to compare classical models, deep learning models, transformer models, and foundation models such as Chronos, TimesFM, and Moirai.

Main research direction:
Towards Trustworthy Foundation Models for Time-Series Forecasting: A Framework for Evaluating Generalisation, Robustness, Uncertainty, and Explainability.

## Current project structure

```text
TimeSeriesFoundationModels/
|-- data/
|   `-- bitcoin/
|       `-- btcusd_1-min_data.csv
|-- figures/
|-- notebooks/
|   |-- 01_EDA.ipynb
|   `-- 02_Classical_Models.ipynb
|-- papers/
|-- proposal/
|-- results/
|-- src/
|   |-- data_loader.py
|   |-- metrics.py
|   |-- plots.py
|   `-- preprocessing.py
|-- README.md
`-- requirements.txt
```

## Bitcoin EDA pipeline modules

- `src/data_loader.py`: loads the raw Bitcoin CSV and converts the Unix-seconds `Timestamp` column to UTC datetimes.
- `src/preprocessing.py`: prepares daily OHLCV Bitcoin data from the minute-level dataset.
- `src/plots.py`: provides a reusable daily time-series plotting helper.
- `src/metrics.py`: contains placeholder metric functions for MAE, RMSE, MAPE, and sMAPE.

Example usage:

```python
from src.data_loader import load_bitcoin_data
from src.preprocessing import prepare_daily_bitcoin_data
from src.plots import plot_time_series

df = load_bitcoin_data("data/bitcoin/btcusd_1-min_data.csv")
df_daily = prepare_daily_bitcoin_data(df)
ax = plot_time_series(df_daily, column="Close")
```
