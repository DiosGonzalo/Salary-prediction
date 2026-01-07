import pickle
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel


print("⏳ Cargando cerebro de la IA...")
with open('modelo_entrenado.pkl', 'rb') as f:
    data = pickle.load(f)

model = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

app = FastAPI(
    title="Salary Predictor API",
    description="API para predecir salarios de desarrolladores basada en Stack Overflow data."
)


class DeveloperInput(BaseModel):
    country: str      
    education: str    
    experience: float 

@app.post("/predict_salary")
def predict_salary(input_data: DeveloperInput):
    

    try:
        country_encoded = le_country.transform([input_data.country])[0]
        education_encoded = le_education.transform([input_data.education])[0]
    except ValueError:
        return {"error": "País o Nivel de estudios no reconocido. Usa los exactos del dataset."}

    features = np.array([[country_encoded, education_encoded, input_data.experience]])


    prediction = model.predict(features)

    return {
        "estimated_salary": round(prediction[0], 2),
        "currency": "USD",
        "profile": {
            "country": input_data.country,
            "experience": input_data.experience
        }
    }


@app.get("/")
def home():
    return {"message": "API de Salarios funcionando correctamente 🚀"}