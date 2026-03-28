from functools import lru_cache
from pathlib import Path

from django.http import HttpResponseNotAllowed
from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


BASE_DIR = Path(__file__).resolve().parent.parent


@lru_cache(maxsize=1)
def get_trained_model():
    data_path = BASE_DIR / "diabetes.csv"
    data = pd.read_csv(data_path)
    X = data.drop("Outcome", axis=1)
    y = data["Outcome"]

    X_train, _, y_train, _ = train_test_split(
        X, y, test_size=0.20, random_state=42
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    return model, X.columns

def home(request):
    return render(request, 'home.html')

def predict(request):
    return render(request, 'predict.html')

def result(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    try:
        model, feature_columns = get_trained_model()

        try:
            payload = request.POST
            val1 = float(payload.get('n1', ''))
            val2 = float(payload.get('n2', ''))
            val3 = float(payload.get('n3', ''))
            val4 = float(payload.get('n4', ''))
            val5 = float(payload.get('n5', ''))
            val6 = float(payload.get('n6', ''))
            val7 = float(payload.get('n7', ''))
            val8 = float(payload.get('n8', ''))
        except ValueError:
            result1 = "Error: Please enter valid numeric values for all fields."
            return render(request, 'predict.html', {"result2": result1})

        # Make predictions
        input_data = pd.DataFrame(
            [[val1, val2, val3, val4, val5, val6, val7, val8]],
            columns=feature_columns,
        )
        pred = model.predict(input_data)[0]

        if pred == 1:
            result1 = "SUSPICIOUS DIABETES RISK POSITIVE"
        else:
            result1 = "HAPPY TO SHARE DIABETES RISK NEGATIVE"

    except FileNotFoundError:
        result1 = "Error: CSV file not found."
    except KeyError:
        result1 = "Error: Dataset format is invalid."
    except Exception:
        result1 = "Error: Prediction service is temporarily unavailable."

    return render(request, 'predict.html', {"result2": result1})
