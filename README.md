# LEJOMER — Reconstrucción de Imágenes

> **Tu imagen, como debe ser.**

Aplicación web de inteligencia artificial orientada a la reconstrucción, restauración y mejora de imágenes que el usuario posee o tiene autorización para editar.

## Objetivo

Desarrollar una plataforma profesional capaz de analizar imágenes, identificar áreas que requieren reconstrucción y generar una versión restaurada mediante técnicas de procesamiento digital e inteligencia artificial.

El proyecto será desarrollado progresivamente utilizando Python, FastAPI, tecnologías de inteligencia artificial, procesamiento de imágenes, bases de datos y una interfaz web moderna.

## Funcionalidades previstas:
- Carga de imágenes individuales.
- Carga de múltiples imágenes.
- Arrastrar y soltar archivos.
- Validación de formatos.
- Análisis automático de imágenes.
- Detección de áreas a reconstruir.
- Reconstrucción mediante inteligencia artificial.
- Comparación antes/después.
- Mejora de resolución.
- Escalado 2x y 4x.
- Procesamiento por lotes.
- Descarga individual.
- Descarga de resultados en ZIP.
- Historial de procesamiento.
- Métricas de calidad.
- Registro del tiempo de procesamiento.
- Analítica del rendimiento de los modelos de IA.

## Formatos compatibles:
- PNG
- JPEG
- JPG
- WEBP
- BMP

## Inteligencia artificial
La arquitectura del proyecto permitirá evaluar diferentes modelos y técnicas de inteligencia artificial para seleccionar las alternativas más adecuadas según:
- Calidad de reconstrucción.
- Tiempo de procesamiento.
- Consumo de memoria.
- Uso de CPU/GPU.
- PSNR.
- SSIM.
- LPIPS.

La selección definitiva del modelo se realizará mediante pruebas y comparación de resultados, evitando depender desde el inicio de un único modelo.

## Arquitectura prevista

```text
Usuario
   │
   ▼
Frontend
   │
   ▼
FastAPI
   │
   ├── Servicio de imágenes
   │
   ├── Servicio de procesamiento
   │
   ├── Pipeline de IA
   │      ├── Preprocesamiento
   │      ├── Detección
   │      ├── Máscara
   │      ├── Reconstrucción
   │      └── Super resolución
   │
   ├── Base de datos
   │
   └── Analítica
