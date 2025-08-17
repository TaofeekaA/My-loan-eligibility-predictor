import joblib
import numpy as np
import pandas as pd

model = joblib.load("models/lr.joblib")

FEATURE_NAMES = ['Gender', 'Married', 'Dependents', 'Education',
       'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Property_Area']

def preprocess_input(user_input):
    mapping = {
        'Married': {'No': 0, "Yes": 1},
        'Gender': {'Male': 1, 'Female': 0},
        'Self_Employed': {'No': 0, 'Yes': 1},
        'Property_Area': {'Rural': 0, "Semiurban": 1, 'Urban': 2},
        'Education': {'Graduate': 1, 'Not Graduate': 0},
        'Dependents': {'0': 0, '1': 1, '2': 2, '3': 3, '3+': 4}
    }

    processed = []
    for feature in FEATURE_NAMES:
        val = user_input[feature]
        if feature in mapping:
            val = mapping[feature][val]
        processed.append(val)

    return np.array(processed).reshape(1, -1)

def make_prediction(user_input):
    try:
        processed_input = preprocess_input(user_input)
        pred = model.predict(processed_input)[0]
        prob = model.predict_proba(processed_input).max()
        return pred, prob
    except Exception as e:
        return f"Error: {str(e)}", 0.0


