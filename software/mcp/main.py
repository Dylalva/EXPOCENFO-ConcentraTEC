import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
import requests


load_dotenv()
app = FastAPI()

API_KEY =  os.getenv('GEMINI_API_KEY')
ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

TEMPLATE = """
Eres un asistente de diagnóstico ergonómico. Recibirás datos ambientales estructurados en el siguiente formato:

Temperatura: {temperature}°C
Humedad relativa: {humidity}%
Sonido: {sound_level} dB
Iluminación: {light_level} lux
Vibración: {vibration_level} m/s²

Tu tarea:
1. Evalúa si el entorno es adecuado para una sesión de trabajo de alta concentración.
2. Da un veredicto claro: “Entorno Adecuado” o “Entorno No Adecuado”.
3. Explica brevemente (1-2 oraciones) cuáles parámetros influyeron más en tu decisión.
4. Propón al menos **tres** recomendaciones prácticas y accionables para mejorar la ergonomía y el confort.
5. Responde en español, de manera concisa y directa.

Por ejemplo:
- “Entorno Adecuado. La temperatura y humedad están dentro del rango óptimo…”
- “Recomendaciones: 1) Bajar el nivel de ruido usando auriculares con cancelación…”

"""

class ContextData(BaseModel):
    sound_level: float
    light_level: float
    vibration_level: float
    temperature: float
    humidity: float

@app.post("/consulta")
def consulta(data: ContextData):
    prompt = TEMPLATE.format(**data.dict())
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"maxOutputTokens": 100}
    }
    headers = {"Content-Type": "application/json"}
    r = requests.post(ENDPOINT, headers=headers, json=payload)

    if r.status_code == 200:
        text = r.json()["candidates"][0]["content"]["parts"][0]["text"]
        return {"respuesta": text}
    else:
        return {"error": r.text}