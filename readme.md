# Student Exam Performance Predictor

A Flask application that predicts a student's math score from demographic
information and reading and writing scores. The project includes a
scikit-learn preprocessing pipeline and trained regression model.

## Requirements

- Python 3.11 (used for validation)
- The packages listed in `requirements.txt`

## Setup

From the project root, create and activate a virtual environment, then install
the dependencies:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run the web app

The checked-in model and preprocessor are used for predictions:

```powershell
python app.py
```

Open the local address printed by Flask in your browser and submit the
prediction form.

## Retrain the model

The training pipeline reads `notebook/data/stud.csv` and writes generated
training data and model files under `artifacts/`. Run it from the project root:

```powershell
python -m src.components.data_ingestion
```

Model training evaluates several regressors and may take some time.