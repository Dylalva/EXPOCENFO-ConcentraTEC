# Avance Preliminar del Proyecto

## 1. Información del Proyecto

* **Nombre del Proyecto:** ConcentraTEC
* **Equipo:** 
  * Alonso Usaga Bonilla.
  * Dylan Elizondo Alvarado.
  * Luis David Salgado Gámez.
  * Jefferson Sandi Ramírez.
* **Roles:**

  * **Líder de Proyecto:** Alonso Usaga Bonilla.
  * **Encargado del LLM:** Dylan Elizondo Alvarado.
  * **Programador Firmware / Backend:** Luis David Salgado Gámez.
  * **Diseñador UX/UI:** Jefferson Sandi Ramírez.

---

## 2. Descripción y Justificación

* **Problema que se aborda:**
  Los entornos de trabajo —especialmente en teletrabajo y espacios flexibles— no se evalúan de forma continua, lo que puede derivar en molestias físicas (dolor de espalda, fatiga visual) y estrés ambiental (ruido, vibraciones).

* **Importancia y contexto:**
  Con el auge del trabajo remoto y modelos híbridos, es vital contar con herramientas que monitoreen en tiempo real las condiciones ergonómicas. Esto reduce riesgos de salud ocupacional y mejora la productividad y bienestar.

* **Usuarios/beneficiarios:**

  * Profesionales en teletrabajo (home office).
  * Oficinas y espacios de coworking.
  * Departamentos de salud ocupacional y recursos humanos.

---

## 3. Objetivos del Proyecto

* **Objetivo General:**
  Desarrollar un sistema integral capaz de diagnosticar dinámicamente la ergonomía de un puesto de trabajo basándose en datos ambientales en tiempo real, y entregar recomendaciones personalizadas al usuario.

* **Objetivos Específicos:**

  1. Integrar sensores de temperatura, humedad, sonido, iluminación y vibración con un ESP32.
  2. Estructurar los datos usando el Model Context Protocol (MCP).
  3. Enviar el paquete MCP al LLM Gemini (Google Cloud) para obtener un diagnóstico ergonómico.
  4. Desplegar los resultados y recomendaciones en una aplicación móvil con interfaz amigable.
  5. Validar el sistema en un piloto con usuarios reales y ajustar umbrales y reportes.

---

## 4. Requisitos Iniciales

* **Hardware y Conectividad:**

  * Placa **ESP32** con Wi-Fi
  * Sensores:

    * Temperatura y humedad (DHT22/SHT31)
    * Sonido (micrófono MAX9814)
    * Iluminación (BH1750 o TSL2561)
    * Vibración (SW-420 o MPU-6050)
  * Actuadores (LED RGB, buzzer) opcionales para feedback local

* **Software y Servicios:**

  * **API Key** de Gemini (Google Cloud)
  * Endpoint:

    ```
    https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent
    ```
  * Librerías:

    * Arduino Core for ESP32
    * Adafruit Sensor / DHT / BH1750 / MPU-6050
    * HTTPClient para ESP32
  * Aplicación móvil (Flutter o React Native)

---

## 5. Diseño Preliminar del Sistema

### 5.1 Arquitectura Inicial


```mermaid
flowchart TB
  %% Sensores
  subgraph sensors["📡 Sensores"]
    direction TB
    T([🌡️ Temperatura])
    H([💧 Humedad])
    S([🔊 Sonido])
    L([💡 Iluminación])
    V([📳 Vibración])
  end

  %% Procesos en Cloud
  subgraph processes["☁️ Procesamiento"]
    direction TB
    MCP([📦 Model Context Protocol])
    LLM([🤖 LLM de diagnóstico])
    FB([🔔 Servicio de Retroalimentación])
  end

  %% Frontend
  subgraph ui["📱 Interfaz Móvil"]
    direction TB
    App([App Móvil])
    User([👤 Usuario])
  end

  %% Flujo de datos
  sensors -->|Datos raw| MCP
  MCP     -->|Payload estructurado| LLM
  LLM     -->|Diagnóstico & recomendaciones| FB
  FB      -->|Notificación Push / API| App
  App     -->|UI Detallada| User

  %% Estilos
  classDef devices   fill:#E1F5FE,stroke:#0277BD,stroke-width:2px,rounded:true;
  classDef services  fill:#E8F5E9,stroke:#2E7D32,stroke-width:2px,rounded:true;
  classDef endpoints fill:#FFF3E0,stroke:#EF6C00,stroke-width:2px,rounded:true;

  class sensors,App,User devices;
  class MCP,LLM,FB services;
```

### 5.2 Componentes previstos

* **Microcontrolador:**

  * ESP32 (dual-core 240 MHz, Wi-Fi/Bluetooth)

* **Sensores / Actuadores:**

  * DHT22/SHT31 (temp. & humedad)
  * MAX9814 (sonido)
  * BH1750/TSL2561 (iluminación)
  * SW-420 o MPU-6050 (vibración)
  * LED RGB y buzzer (feedback local)

* **LLM / API:**

  * Google Gemini v2.0-flash (nube)
  * Autenticación por X-goog-api-key

* **Librerías y Herramientas:**

  * Arduino ESP32 Core
  * Adafruit Sensor Suite
  * HTTPClient (ESP32)
  * Kotlin para la app móvil

### 5.3 Bocetos o esquemas


---

## 6. Plan de Trabajo

| Hito                                 | Fecha Estimada |
| ------------------------------------ | -------------- |
| Recopilación de requisitos           | 15 ago 2025    |
| Prototipo HW con ESP32 y sensores    | 30 sept 2025   |
| Integración MCP + LLM Gemini         | 15 oct 2025    |
| Desarrollo de app móvil (v1.0)       | 30 nov 2025    |
| Pruebas piloto con usuarios beta     | 15 dic 2025    |
| Ajustes finales y entrega de informe | 15 ene 2026    |

### Riesgos y Mitigaciones

* **Conectividad Wi-Fi inestable**
  *Mitigación:* Buffer local y reintentos automáticos.

* **Latencia al invocar LLM**
  *Mitigación:* Cache de respuestas recientes y fallback local con reglas heurísticas.

* **Precisión/calibración de sensores**
  *Mitigación:* Calibración previa y filtros de software.

* **Gestión segura de la API Key**
  *Mitigación:* Uso de variables de entorno y backend proxy; no almacenar en firmware público.

---

## 7. Prototipos Conceptuales