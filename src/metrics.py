"""Forecast evaluation metrics."""

import numpy as np


def _as_arrays(y_true, y_pred):
    """Convert metric inputs to aligned NumPy arrays."""
    true = np.asarray(y_true, dtype=float)
    pred = np.asarray(y_pred, dtype=float)

    if true.shape != pred.shape:
        raise ValueError("y_true and y_pred must have the same shape.")

    mask = ~(np.isnan(true) | np.isnan(pred))
    return true[mask], pred[mask]


def mae(y_true, y_pred):
    """Calculate mean absolute error."""
    true, pred = _as_arrays(y_true, y_pred)
    return np.mean(np.abs(true - pred))


def rmse(y_true, y_pred):
    """Calculate root mean squared error."""
    true, pred = _as_arrays(y_true, y_pred)
    return np.sqrt(np.mean((true - pred) ** 2))


def mape(y_true, y_pred):
    """Calculate mean absolute percentage error as a percentage."""
    true, pred = _as_arrays(y_true, y_pred)
    nonzero = true != 0
    return np.mean(np.abs((true[nonzero] - pred[nonzero]) / true[nonzero])) * 100


def smape(y_true, y_pred):
    """Calculate symmetric mean absolute percentage error as a percentage."""
    true, pred = _as_arrays(y_true, y_pred)
    denominator = np.abs(true) + np.abs(pred)
    nonzero = denominator != 0
    return np.mean(2 * np.abs(pred[nonzero] - true[nonzero]) / denominator[nonzero]) * 100
