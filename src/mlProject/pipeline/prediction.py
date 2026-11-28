import joblib
import numpy as np
import pandas as pd
from pathlib import Path


# class PredictionPipeline:
#     def __init__(self):
#         self.model = joblib.load(Path("artifacts/model_trainer/model.joblib"))

#     def predict(self, data):
#         prediction = self.model.predict(data)

#         return prediction

class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(
            Path("artifacts/model_trainer/model.joblib")
        )

        print("Model expects:")
        print(self.model.feature_names_in_)

    def predict(self, data):
        print("Incoming columns:")
        print(data.columns.tolist())

        prediction = self.model.predict(data)

        return prediction