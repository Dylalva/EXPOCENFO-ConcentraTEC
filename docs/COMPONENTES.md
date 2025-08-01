# Descripción de Componentes

* **Microcontroladores**

  * **ESP32**

    * CPU dual-core a 240 MHz
    * Wi-Fi y Bluetooth integrados
    * ADC/DAC, I²C, SPI, UART, PWM, GPIOs múltiples

* **Sensores / Actuadores**

  * **Sensor de temperatura y humedad**
    * Ej. DHT22 o SHT31 (interfaz digital, I²C o 1-wire)
  
  * **Sensor de sonido**

    * Módulo micrófono electret con amplificador (p. ej. MAX9814) conectado a ADC
  * **Sensor de iluminación**

    * BH1750 o TSL2561 (I²C) para medir lux
  * **Sensor de vibración**

    * SW-420 o acelerómetro de 3 ejes (p. ej. MPU-6050) según nivel de detalle
  * **Actuadores / Indicadores**

    * LED RGB (estado: óptimo / alerta)
    * Buzzer piezoeléctrico para alarmas locales
    * (Opcional) Pantalla OLED 0.96″
    
* **LLM empleado**

  * **Gemini (Google Cloud)**

    * Modelo en la nube accesible vía API de Generative Language
    * Se integra usando el **X-goog-api-key** y el endpoint
      `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent`
    * Procesamiento remoto (cloud) para síntesis y recomendaciones ergonómicas.
