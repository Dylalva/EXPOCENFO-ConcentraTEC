# 🛠️ Despliegue de Servidor FastAPI en Render para Diagnóstico Ergonómico

Este proyecto despliega una API REST en FastAPI que utiliza el modelo **Gemini 1.5 Flash** de Google para evaluar condiciones ergonómicas en entornos de trabajo, y generar recomendaciones prácticas.

---

## 🚀 Despliegue en Render

### 1. Crea una cuenta en Render

* Ingresa a [Render](https://render.com).
* Regístrate o inicia sesión.

### 2. Crea un nuevo repositorio en GitHub

* Asegúrate de subir tu proyecto con los siguientes archivos:

  * `main.py`
  * `render.yml`
  * `requirements.txt`
  * `.env` (⚠️ No subir este archivo si contiene claves privadas; Render permite definir variables de entorno desde su panel)

### 3. Conecta GitHub con Render

* Desde el dashboard de Render:

  * Haz clic en **"New + > Web Service"**.
  * Elige el repositorio que contiene tu proyecto.

### 4. Render detectará automáticamente el archivo `render.yml`

Este archivo configura el servicio, incluyendo:

```yaml
services:
  - type: web                # Tipo de servicio web
    name: mcp-concentratec   # Nombre del servicio
    env: python              # Entorno de ejecución
    plan: free               # Plan gratuito
    buildCommand: pip install -r requirements.txt  # Instalación de dependencias
    startCommand: uvicorn main:app --host 0.0.0.0 --port 10000  # Comando para iniciar la API
```

### 5. Agrega las variables de entorno

Desde el panel de configuración del servicio en Render:

* Ve a **"Environment > Environment Variables"**
* Agrega:

  * `GEMINI_API_KEY`: tu clave API de [Google AI Studio](https://aistudio.google.com/app/apikey)

### 6. Espera a que se construya el servicio

* Render instalará dependencias, iniciará la aplicación con Uvicorn y generará una URL pública del tipo:
  `https://mcp-melodia.onrender.com`

### 7. Prueba tu API

* Endpoint disponible: `POST /consulta`
* Cuerpo del JSON de prueba:

```json
{
  "sound_level": 50,
  "light_level": 300,
  "vibration_level": 0.1,
  "temperature": 24,
  "humidity": 45
}
```

---

## 📄 Descripción del código

### `main.py`

#### 1. Librerías usadas:

```python
from dotenv import load_dotenv           # Carga variables de entorno desde un archivo .env
from fastapi import FastAPI              # Framework para construir APIs web
from pydantic import BaseModel           # Validación de datos de entrada
import requests                          # Permite hacer peticiones HTTP
```

#### 2. Inicialización y carga de clave:

```python
load_dotenv()                            # Carga variables desde .env
API_KEY = os.getenv('GEMINI_API_KEY')    # Clave API del modelo Gemini
```

#### 3. Configuración de FastAPI:

```python
app = FastAPI()
```

#### 4. Template del mensaje:

Este prompt se enviará al modelo de lenguaje con los datos ambientales:

```python
TEMPLATE = """
Eres un asistente de diagnóstico ergonómico...
"""
```

#### 5. Esquema de entrada (usando Pydantic):

```python
class ContextData(BaseModel):
    sound_level: float
    light_level: float
    vibration_level: float
    temperature: float
    humidity: float
```

#### 6. Endpoint `/consulta`:

```python
@app.post("/consulta")
def consulta(data: ContextData):
```

* Toma los datos del entorno como JSON.
* Construye el `prompt` a partir del `TEMPLATE`.
* Llama a la API de Gemini para obtener una respuesta.
* Devuelve el texto generado por el modelo o un mensaje de error.

---

## 🧪 Ejemplo de respuesta esperada

```json
{
  "respuesta": "Entorno No Adecuado. El nivel de ruido y la vibración son elevados... Recomendaciones: 1) Usa auriculares con cancelación, 2) Mejora el aislamiento acústico, 3) Reduce vibraciones del escritorio."
}
```

---

## 📦 `requirements.txt`

Asegúrate de incluir:

```
python-dotenv
fastapi
uvicorn
requests
```

---

## ✅ Notas finales

* Render reiniciará el servidor automáticamente al detectar cambios en el repositorio.
* Puedes escalar el servicio a planes pagos si necesitas más recursos o disponibilidad.
* El endpoint está listo para ser consumido desde interfaces web, móviles o scripts de automatización.
