# Arquitectura del Software

## LEJOMER — Reconstrucción de Imágenes

**Versión:** 1.0  
**Estado:** Diseño inicial

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 1. Objetivo
Este documento define la arquitectura técnica inicial del sistema LEJOMER — Reconstrucción de Imágenes.
La arquitectura busca mantener una separación clara entre la interfaz de usuario, la API, los servicios de procesamiento, los modelos de inteligencia artificial, la base de datos y la analítica.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 2. Arquitectura general
El sistema estará organizado mediante diferentes capas y servicios.

```text
                    USUARIO
                       │
                       ▼
                ┌─────────────┐
                │  FRONTEND   │
                │ React / Web │
                └──────┬──────┘
                       │
                       ▼
                ┌─────────────┐
                │   FASTAPI   │
                │     API     │
                └──────┬──────┘
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
     ┌─────────┐ ┌────────────┐ ┌───────────┐
     │ Imágenes│ │Procesamiento││ Resultados│
     │ Service │ │   Service   ││  Service  │
     └────┬────┘ └──────┬─────┘ └─────┬─────┘
          │             │              │
          │             ▼              │
          │      ┌─────────────┐       │
          │      │ PIPELINE IA │       │
          │      └──────┬──────┘       │
          │             │              │
          │     ┌───────┼────────┐     │
          │     ▼       ▼        ▼     │
          │ Detección Reconstrucción   │
          │             │       Super  │
          │             │     Resolución
          │             └────────┬─────┘
          │                      │
          ▼                      ▼
     ┌───────────┐         ┌───────────┐
     │PostgreSQL │         │ Archivos  │
     └───────────┘         └───────────┘
                                │
                                ▼
                         ┌────────────┐
                         │ ANALÍTICA  │
                         └────────────┘

