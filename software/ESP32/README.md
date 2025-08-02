# 🌐 Diagnóstico Ergonómico con ESP32 + FastAPI + Gemini

Este proyecto conecta un microcontrolador **ESP32** a un servidor en la nube (desplegado con **Render**) que evalúa datos ambientales simulados usando la API de lenguaje **Gemini 1.5 Flash** de Google. La finalidad es diagnosticar si el entorno de trabajo es ergonómicamente adecuado y ofrecer recomendaciones.

---

## 🔁 Flujo del Sistema

1. El **ESP32** simula datos ambientales: temperatura, humedad, ruido, luz y vibración.
2. Envía estos datos a una API REST desplegada con **FastAPI**.
3. La API consulta a **Gemini** para analizar los datos y generar un diagnóstico.
4. El resultado se imprime en el monitor serial del ESP32.

---

## 📦 Estructura

```
.
├── code.py               ← Código para el ESP32
├── secrets_MCP.py        ← Configuración del ESP32 (Wi-Fi y URL)
└── README.md             ← Esta documentación
```

---

## ☁️ Parte 1: Despliegue del Servidor en Render

> Si ya hiciste esto, puedes saltar a la Parte 2.

1. Sube los archivos `main.py`, `render.yml`, `requirements.txt` a un repositorio en GitHub.
2. Crea un nuevo Web Service en [Render](https://render.com).
3. Define la variable de entorno `GEMINI_API_KEY` con tu clave de Google AI Studio.
4. Espera a que Render genere tu URL pública, por ejemplo:
   `https://mcp-concentratex.onrender.com`

Para más detalles, consulta el [README del servidor](../mcp/README.md).

---

## 📡 Parte 2: Carga y Ejecución del Cliente en ESP32

### 🔧 Requisitos

* ESP32 con MicroPython instalado.
* Herramientas como [Thonny](https://thonny.org/) o [mpremote](https://docs.micropython.org/en/latest/reference/mpremote.html).
* Archivos necesarios:

  * `esp32_client.py` → tu código principal.
  * `secrets_MCP.py` → tus credenciales Wi-Fi y URL.

### 📁 `secrets_MCP.py` (configura antes de subirlo):

```python
secrets = {
    "ssid": "NOMBRE_DE_TU_WIFI",
    "password": "CONTRASEÑA_WIFI",
    "url_mcp": "https://mcp-concentratec.onrender.com"
}
```

### 🚀 Subir código al ESP32

Puedes usar Thonny o ejecutar desde terminal:

```bash
mpremote connect ttyUSB0 fs cp esp32_client.py :
mpremote connect ttyUSB0 fs cp secrets_MCP.py :
```

> Reemplaza `ttyUSB0` según tu sistema operativo.

---

## 🧠 ¿Qué hace el ESP32?

```python
# 1) Simula lecturas de sensores
# 2) Envía un JSON al endpoint /consulta
# 3) Imprime en consola el diagnóstico generado por Gemini
# 4) Espera 60 segundos y repite
```

Ejemplo de salida por el monitor serial:

```
Enviando datos: {"temperature": 24.3, "humidity": 48.0, ...}
Status: 200
Respuesta del LLM: Entorno Adecuado. La iluminación es óptima y no hay niveles de vibración relevantes...
```

---

## 🧪 Pruebas Manuales

También puedes probar el servidor desde herramientas como Postman o `curl`:

```bash
curl -X POST https://<TU-URL>.onrender.com/consulta \
  -H "Content-Type: application/json" \
  -d '{"temperature":24,"humidity":50,"sound_level":40,"light_level":400,"vibration_level":0.2}'
```

---

## 📌 Notas finales

* El sistema es completamente funcional sin sensores físicos gracias a la simulación.
* Puedes reemplazar las funciones simuladas por lecturas reales (DHT22, micrófono, LDR, etc.).
* Usa la respuesta generada para encender LEDs, enviar alertas, o mostrar en una pantalla OLED.

---

## ✅ Recursos recomendados

* [MicroPython para ESP32](https://micropython.org/download/esp32/)
* [FastAPI Docs](https://fastapi.tiangolo.com/)
* [Google AI Studio](https://aistudio.google.com/)
* [Render.com Docs](https://render.com/docs)
