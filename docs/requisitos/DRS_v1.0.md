# Documento de Requisitos de Software

## LEJOMER — Reconstrucción de Imágenes

**Versión:** 1.0  
**Estado:** Inicial  
**Proyecto:** LEJOMER — Reconstrucción de Imágenes

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 1. Introducción

### 1.1 Propósito
Este documento define los requisitos funcionales y no funcionales del sistema LEJOMER — Reconstrucción de Imágenes.
El sistema será una aplicación web orientada al procesamiento, reconstrucción y mejora de imágenes mediante técnicas de procesamiento digital e inteligencia artificial.

### 1.2 Objetivo del sistema
El objetivo es desarrollar una plataforma que permita al usuario cargar imágenes autorizadas para su edición, analizarlas, procesarlas y obtener resultados reconstruidos o mejorados.

### 1.3 Alcance
El sistema contempla:
- Carga de imágenes.
- Validación de archivos.
- Procesamiento individual.
- Procesamiento por lotes.
- Reconstrucción mediante IA.
- Mejora de resolución.
- Comparación antes/después.
- Descarga de resultados.
- Historial de procesamiento.
- Métricas de calidad.
- Analítica del procesamiento.

--------------------------------------------------------------------------------------------------------------------------

## 2. Formatos soportados
El sistema permitirá inicialmente imagenes:
- PNG
- JPEG
- JPG
- WEBP
- BMP

--------------------------------------------------------------------------------------------------------------------------

## 3. Requisitos funcionales
### RF-01 — Cargar una imagen
El sistema deberá permitir al usuario cargar una imagen individual.

### RF-02 — Cargar múltiples imágenes
El sistema deberá permitir cargar múltiples imágenes para procesamiento por lotes.

### RF-03 — Validar archivos
El sistema deberá verificar que los archivos correspondan a formatos permitidos y cumplan las restricciones establecidas.

### RF-04 — Analizar imagen
El sistema deberá analizar automáticamente la imagen recibida para identificar las áreas que requieren procesamiento.

### RF-05 — Reconstruir imagen
El sistema deberá generar una versión reconstruida utilizando técnicas de procesamiento de imágenes e inteligencia artificial.

### RF-06 — Mejorar resolución
El sistema deberá permitir seleccionar diferentes niveles de resolución, inicialmente:
- Original
- 2x
- 4x

### RF-07 — Comparar resultados
El sistema deberá permitir visualizar la imagen original y el resultado procesado.

### RF-08 — Descargar resultado
El sistema deberá permitir descargar individualmente el resultado generado.

### RF-09 — Descargar procesamiento por lotes
El sistema deberá permitir descargar múltiples resultados mediante un archivo ZIP.

### RF-10 — Consultar historial
El sistema deberá registrar y permitir consultar los procesos realizados.

### RF-11 — Registrar métricas
El sistema deberá registrar métricas relacionadas con calidad y rendimiento.

----------------------------------------------------------------------------------------------------------------

## 4. Requisitos no funcionales
### RNF-01 — Usabilidad
La interfaz deberá ser clara y sencilla para usuarios con diferentes niveles de conocimiento técnico.

### RNF-02 — Rendimiento
El sistema deberá informar el estado y progreso de los procesos que puedan requerir tiempos prolongados.

### RNF-03 — Seguridad
El sistema deberá validar archivos y controlar el acceso a los resultados de procesamiento.

### RNF-04 — Escalabilidad
La arquitectura deberá permitir incorporar nuevos modelos de inteligencia artificial y nuevas funcionalidades.

### RNF-05 — Mantenibilidad
El código deberá organizarse mediante componentes y servicios independientes.

### RNF-06 — Portabilidad
El sistema deberá poder ejecutarse mediante Docker para facilitar su despliegue.

----------------------------------------------------------------------------------------------------------------

## 5. Restricciones
- El sistema deberá utilizar Python para el backend.
- El backend utilizará FastAPI.
- El procesamiento podrá utilizar Pillow y OpenCV.
- Los modelos de IA podrán implementarse mediante PyTorch.
- La base de datos prevista será PostgreSQL.
- El proyecto utilizará Git y GitHub para control de versiones.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 6. Uso responsable
> Esta herramienta está destinada a eliminar marcas de agua que usuario posee o tiene derechos para usar. Asegúrese de que su uso cumpla con las leyes de derechos de autor aplicables.
El sistema deberá utilizarse únicamente con imágenes sobre las cuales el usuario tenga propiedad, autorización o los derechos necesarios para realizar modificaciones.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 7. Estado del documento
**Versión:** 1.0  
**Estado:** Documento inicial de requisitos.
