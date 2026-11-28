from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

from mlProject.pipeline.prediction import PredictionPipeline

app = FastAPI()

class WineData(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/predict")
def predict(data: WineData):
    df = pd.DataFrame([data.model_dump()])

    df.rename(columns={
        "fixed_acidity": "fixed acidity",
        "volatile_acidity": "volatile acidity",
        "citric_acid": "citric acid",
        "residual_sugar": "residual sugar",
        "free_sulfur_dioxide": "free sulfur dioxide",
        "total_sulfur_dioxide": "total sulfur dioxide"
    }, inplace=True)
    pipeline = PredictionPipeline()
    prediction = pipeline.predict(df)

    return {"prediction": float(prediction[0])}

# import uvicorn

# if __name__ == "__main__":
#     uvicorn.run(
#         "api:app",
#         host="0.0.0.0",
#         port=8080,
#         reload=True
#     )