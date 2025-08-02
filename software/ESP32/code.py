import time
import urequests
import ujson
import random
import wifi
from secrets_MCP import secrets

SERVER   = secrets["url_mcp"] + "/consulta"
# ————— Configuración Wi-Fi —————

wifi.radio.connect(secrets["ssid"], secrets["password"])

# ————— Funciones de datos simulados —————
def read_temperature():
    return round(random.random() * 6 + 20, 1)

def read_humidity():
    return round(random.random() * 30 + 30, 1)

def read_sound_level():
    return round(random.random() * 40 + 30, 1)

def read_light_level():
    return round(random.random() * 700 + 100, 1)

def read_vibration_level():
    return round(random.random() * 0.5, 2)

# ————— Bucle principal —————
while True:
    # 1) Generar datos simulados
    payload = {
        "temperature":     read_temperature(),
        "humidity":        read_humidity(),
        "sound_level":     read_sound_level(),
        "light_level":     read_light_level(),
        "vibration_level": read_vibration_level()
    }
    body = ujson.dumps(payload)

    # 2) Enviar al servidor FastAPI
    try:
        print("Enviando datos:", body)
        resp = urequests.post(SERVER, headers={'Content-Type':'application/json'}, data=body)
        print("Status:", resp.status_code)
        print("Respuesta del LLM:", resp.text)
        resp.close()
    except Exception as e:
        print("Error al enviar:", e)

    # 3) Esperar antes de la próxima simulación
    time.sleep(60)
