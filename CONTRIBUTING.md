# 🤝 Guía de Contribución - ConcentraTEC

## 📋 Cómo Contribuir

### 1. Fork y Clone
```bash
git clone https://github.com/Dylalva/EXPOCENFO-ConcentraTEC.git
cd EXPOCENFO-ConcentraTEC
```

### 2. Crear Branch
```bash
git checkout -b feature/nombre-descriptivo
```

### 3. Realizar Cambios
- Sigue las convenciones de código existentes
- Documenta cambios significativos
- Prueba tu código antes de enviar

### 4. Commit y Push
```bash
git add .
git commit -m "feat: descripción clara del cambio"
git push origin feature/nombre-descriptivo
```

### 5. Pull Request
- Describe claramente los cambios realizados
- Incluye capturas si hay cambios visuales
- Referencia issues relacionados

## 🏗️ Estructura del Proyecto

```
├── docs/           # Documentación
├── hardware/       # Esquemas y diagramas
├── software/       # Código fuente
│   ├── ESP32/      # Firmware microcontrolador
│   └── mcp/        # Servidor backend
├── tests/          # Pruebas
└── examples/       # Ejemplos de uso
```

## 📝 Convenciones

### Commits
- `feat:` nueva funcionalidad
- `fix:` corrección de bugs
- `docs:` cambios en documentación
- `refactor:` refactorización de código
- `test:` añadir o modificar tests

### Código
- **Python**: PEP 8
- **Documentación**: Markdown con enlaces relativos
- **Variables**: nombres descriptivos en inglés
- **Comentarios**: explicar el "por qué", no el "qué"

### Archivos
- Usar UTF-8
- Líneas terminadas en LF
- Máximo 100 caracteres por línea

## 🧪 Testing

### ESP32
```bash
# Simular en local antes de subir al hardware
python software/ESP32/code.py
```

### Backend
```bash
cd software/mcp
pip install -r requirements.txt
uvicorn main:app --reload
```

## 📚 Documentación

- Actualizar `docs/README.md` si añades nueva documentación
- Incluir ejemplos de uso para nuevas funcionalidades
- Mantener diagramas actualizados

## 🐛 Reportar Issues

1. Buscar issues existentes primero
2. Usar plantillas disponibles
3. Incluir:
   - Descripción clara del problema
   - Pasos para reproducir
   - Comportamiento esperado vs actual
   - Logs/capturas relevantes

## 👥 Equipo

| Rol | Responsable | Área |
|-----|-------------|------|
| Líder | Alonso Usaga | Coordinación general |
| LLM | Dylan Elizondo | Integración Gemini |
| Backend | Luis Salgado | ESP32 y servidor |
| UX/UI | Jefferson Sandi | Diseño e interfaz |

## ✅ Checklist Pre-Commit

- [ ] Código funciona localmente
- [ ] Documentación actualizada
- [ ] Commits siguen convenciones
- [ ] No hay credenciales expuestas
- [ ] Tests pasan (si aplica)

---

¡Gracias por contribuir a ConcentraTEC! 🚀