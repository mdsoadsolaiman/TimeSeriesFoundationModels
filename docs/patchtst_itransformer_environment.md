# PatchTST and iTransformer Environment

This project keeps the main Python 3.13.2 `.venv` unchanged. Use a separate
Python 3.11 or Python 3.12 environment for modern Transformer forecasting
models such as PatchTST and iTransformer.

## Why a Separate Environment Is Required

The current Python 3.13.2 environment cannot install NeuralForecast normally
with all declared dependencies because NeuralForecast depends on Ray and Ray is
not available for this environment through pip:

```text
ERROR: No matching distribution found for ray
```

A manual `--no-deps` NeuralForecast install could bypass Ray, but this project
intentionally does **not** use that workaround because it is not fully
dependency-compliant. PatchTST and iTransformer should run in a supported
Python 3.11 or Python 3.12 environment instead.

## Current Setup Blocker

The Windows Python launcher is not currently available in this shell:

```powershell
py -3.11 --version
```

Observed error:

```text
py : The term 'py' is not recognized as the name of a cmdlet, function, script file, or operable program.
```

No standalone Python 3.11 or Python 3.12 executable was found either. Install
Python 3.11 or Python 3.12 with the Windows launcher enabled, or provide the
absolute path to a supported Python executable, before creating the modern
forecasting environment.

## Create the Python 3.11 or 3.12 Environment

Run these commands from the repository root:

```powershell
py -3.11 -m venv .venv-modern
.\.venv-modern\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheel
pip install numpy pandas matplotlib scikit-learn jupyter torch
pip install "pytorch-lightning<2.6"
pip install neuralforecast
```

If Python 3.12 is preferred and available through the launcher, use:

```powershell
py -3.12 -m venv .venv-modern
```

## Verify NeuralForecast Imports

After installation, verify that PatchTST and iTransformer are available:

```powershell
python -c "from neuralforecast import NeuralForecast; from neuralforecast.models import PatchTST, iTransformer; print('NeuralForecast modern imports OK')"
```

Equivalent Python check:

```python
from neuralforecast import NeuralForecast
from neuralforecast.models import PatchTST, iTransformer
```

Only create or run `notebooks/05_Modern_Transformers.ipynb` after these imports
pass inside `.venv-modern`.

## Notebook Scope

The modern Transformer notebook should:

- Use `src.data_loader.load_bitcoin_data`.
- Use `src.preprocessing.prepare_daily_bitcoin_data`.
- Use `src.metrics.mae`, `rmse`, `mape`, and `smape`.
- Use the Bitcoin daily `Close` series.
- Use the same 80/20 chronological train-test split as the other notebooks.
- Evaluate PatchTST and iTransformer only after their imports pass.
- Compare against Naive, 7-Day Moving Average, LSTM, and Corrected Transformer
  benchmarks.
- Report MAE, RMSE, MAPE, and sMAPE.
- Plot forecasts against the test set.
