"""Plotting helpers for exploratory time-series analysis."""

import matplotlib.pyplot as plt


def plot_time_series(df_daily, column="Close"):
    """Plot a daily time series column.

    Parameters
    ----------
    df_daily : pandas.DataFrame
        Daily Bitcoin data indexed by date, or containing a ``Timestamp`` column.
    column : str, default="Close"
        Column to plot.

    Returns
    -------
    matplotlib.axes.Axes
        The axes containing the line plot.
    """
    if column not in df_daily.columns:
        raise ValueError(f"Column '{column}' not found in daily data.")

    plot_df = df_daily
    x_values = plot_df.index
    x_label = "Date"

    if "Timestamp" in plot_df.columns:
        x_values = plot_df["Timestamp"]

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(x_values, plot_df[column], linewidth=1.5)
    ax.set_title(f"Bitcoin Daily {column}")
    ax.set_xlabel(x_label)
    ax.set_ylabel(column)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return ax

