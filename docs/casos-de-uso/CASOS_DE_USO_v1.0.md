# CASOS DE USO — LEJOMER Reconstrucción de Imágenes

**Versión:** 1.0  
**Proyecto:** LEJOMER — Reconstrucción de Imágenes  
**Repositorio:** lejomer-image-reconstruction  
**Estado:** Documento inicial  

-----------------------------------------------------------------------------------------------------------------------------------

## 1. Introducción
Este documento define los principales casos de uso del sistema LEJOMER — Reconstrucción de Imágenes.
Los casos de uso describen las acciones que puede realizar un usuario dentro de la aplicación y la respuesta esperada del sistema.
La aplicación está orientada al procesamiento de imágenes que el usuario posee o tiene autorización para editar.

-----------------------------------------------------------------------------------------------------------------------------------

## 2. Actores

### 2.1 Usuario
Persona que utiliza la aplicación para cargar, analizar, reconstruir, mejorar y descargar imágenes.

### 2.2 Sistema LEJOMER
Componente responsable de recibir las imágenes, validarlas, procesarlas, ejecutar los servicios de inteligencia artificial, almacenar los resultados y presentar la información al usuario.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3. Casos de uso principales

## CU-01 — Cargar una imagen

### Objetivo
Permitir al usuario seleccionar y cargar una imagen para iniciar el procesamiento.

### Actor principal
Usuario.

### Precondiciones
- El usuario debe encontrarse en la aplicación.
- La imagen debe estar en un formato compatible.

### Flujo principal
1. El usuario selecciona una imagen.
2. El sistema recibe el archivo.
3. El sistema valida el formato.
4. El sistema valida el tamaño del archivo.
5. El sistema obtiene las dimensiones de la imagen.
6. El sistema registra la información de la imagen.
7. El sistema muestra una vista previa.
8. El sistema permite continuar con el procesamiento.

### Resultado
La imagen queda preparada para ser analizada.

### Excepciones
- Formato no compatible.
- Archivo demasiado grande.
- Archivo corrupto.
- Error durante la carga.

-----------------------------------------------------------------------------

# CU-02 — Cargar múltiples imágenes

### Objetivo
Permitir al usuario seleccionar varias imágenes para procesamiento por lotes.

### Actor principal
Usuario.

### Precondiciones
- La aplicación debe estar disponible.
- Los archivos deben cumplir los formatos permitidos.

### Flujo principal
1. El usuario selecciona múltiples imágenes.
2. El sistema recibe los archivos.
3. El sistema valida cada archivo.
4. El sistema identifica los archivos válidos.
5. El sistema informa los archivos rechazados.
6. El sistema crea un trabajo de procesamiento.
7. El sistema muestra el progreso.

### Resultado
Las imágenes válidas quedan asociadas a un trabajo de procesamiento por lotes.

-----------------------------------------------------------------------------------

# CU-03 — Analizar una imagen

### Objetivo
Analizar automáticamente una imagen para identificar las áreas que requieren reconstrucción.

### Actor principal
Usuario.

### Precondiciones
- La imagen debe haber sido cargada correctamente.

### Flujo principal
1. El usuario inicia el análisis.
2. El sistema prepara la imagen.
3. El sistema ejecuta el análisis mediante el servicio de inteligencia artificial.
4. El sistema identifica las áreas relevantes.
5. El sistema genera una máscara de procesamiento.
6. El sistema presenta el resultado preliminar.

### Resultado
El sistema dispone de información necesaria para realizar la reconstrucción.

--------------------------------------------------------------------------------------

# CU-04 — Detectar automáticamente el área de reconstrucción

### Objetivo
Identificar automáticamente las zonas de la imagen que deben ser reconstruidas.

### Actor principal
Sistema LEJOMER.

### Precondiciones
- La imagen debe haber sido cargada.
- El sistema de análisis debe estar disponible.

### Flujo principal
1. El sistema analiza la imagen.
2. El modelo de inteligencia artificial identifica el área objetivo.
3. El sistema genera una máscara.
4. El sistema valida la máscara.
5. El sistema envía la información al servicio de reconstrucción.

### Resultado
Se obtiene una máscara que delimita el área que será procesada.

-------------------------------------------------------------------------------------------------------------------

# CU-05 — Reconstruir una imagen

### Objetivo
Generar una versión reconstruida de una imagen utilizando técnicas de procesamiento e inteligencia artificial.

### Actor principal
Usuario.

### Precondiciones
- La imagen debe estar cargada.
- Debe existir una máscara válida.
- El servicio de reconstrucción debe estar disponible.

### Flujo principal
1. El usuario inicia la reconstrucción.
2. El sistema prepara la imagen.
3. El sistema utiliza la máscara generada.
4. El modelo de reconstrucción procesa el área seleccionada.
5. El sistema genera una nueva imagen.
6. El sistema guarda el resultado.
7. El sistema registra información del procesamiento.

### Resultado
Se genera una imagen reconstruida.

----------------------------------------------------------------------------

# CU-06 — Aumentar la resolución

### Objetivo
Permitir mejorar la resolución de la imagen procesada.

### Actor principal
Usuario.

### Precondiciones
- Debe existir una imagen procesada.
- El servicio de super resolución debe estar disponible.

### Flujo principal
1. El usuario selecciona la opción de mejora de resolución.
2. El usuario selecciona el factor de escala.
3. El sistema valida la opción seleccionada.
4. El sistema ejecuta el procesamiento.
5. El sistema genera la imagen de mayor resolución.
6. El sistema registra el resultado.

### Factores iniciales
- Original.
- 2x.
- 4x.

### Resultado
Se obtiene una versión de mayor resolución.

-----------------------------------------------------------------------------------------------------------

# CU-07 — Comparar imagen original y resultado

### Objetivo
Permitir al usuario comparar visualmente la imagen original con la imagen procesada.

### Actor principal
Usuario.

### Precondiciones
- Debe existir una imagen original.
- Debe existir un resultado procesado.

### Flujo principal
1. El usuario abre la comparación.
2. El sistema muestra la imagen original.
3. El sistema muestra la imagen procesada.
4. El usuario puede desplazar el control de comparación.
5. El sistema actualiza la visualización.

### Resultado
El usuario puede evaluar visualmente el resultado obtenido.

-------------------------------------------------------------------------------------------

# CU-08 — Descargar resultado individual

### Objetivo
Permitir al usuario descargar una imagen procesada.

### Actor principal
Usuario.

### Precondiciones
- Debe existir un resultado disponible.

### Flujo principal
1. El usuario selecciona un resultado.
2. El usuario pulsa descargar.
3. El sistema prepara el archivo.
4. El sistema inicia la descarga.

### Resultado
El usuario obtiene el archivo procesado.

---------------------------------------------------------------------------------------

# CU-09 — Descargar resultados en ZIP

### Objetivo
Permitir descargar múltiples resultados agrupados en un archivo ZIP.

### Actor principal
Usuario.

### Precondiciones
- Deben existir uno o más resultados procesados.

### Flujo principal
1. El usuario selecciona un trabajo.
2. El usuario solicita la descarga.
3. El sistema identifica los resultados.
4. El sistema genera un archivo ZIP.
5. El sistema inicia la descarga.

### Resultado
El usuario obtiene un archivo ZIP con los resultados procesados.

--------------------------------------------------------------------------------------

# CU-10 — Consultar historial

### Objetivo
Permitir al usuario consultar los trabajos realizados anteriormente.

### Actor principal
Usuario.

### Precondiciones
- Deben existir trabajos registrados.

### Flujo principal
1. El usuario ingresa al historial.
2. El sistema consulta los trabajos registrados.
3. El sistema muestra los trabajos.
4. El usuario selecciona un trabajo.
5. El sistema muestra la información correspondiente.

### Información mostrada
- Fecha.
- Cantidad de imágenes.
- Estado.
- Tiempo de procesamiento.
- Modelo utilizado.
- Resultados disponibles.

### Resultado
El usuario puede consultar sus procesos anteriores.

----------------------------------------------------------------------------------------

# CU-11 — Consultar métricas del procesamiento

### Objetivo
Mostrar información cuantitativa sobre el rendimiento y calidad del procesamiento.

### Actor principal
Usuario.

### Precondiciones
- Debe existir un resultado procesado.
- Deben existir métricas calculadas.

### Métricas iniciales
- PSNR.
- SSIM.
- LPIPS.
- Tiempo de procesamiento.
- Uso de GPU.
- Uso de memoria.

### Flujo principal
1. El usuario consulta un resultado.
2. El sistema consulta las métricas.
3. El sistema muestra los valores.
4. El usuario puede utilizar la información para evaluar el resultado.

### Resultado

El usuario obtiene información cuantitativa sobre el procesamiento.

-------------------------------------------------------------------------------

# 4. Resumen de casos de uso

| Código |           Caso de uso           | Actor principal |
|--------|---------------------------------|-----------------|
| CU-01  | Cargar una imagen               |      Usuario    |
| CU-02  | Cargar múltiples imágenes       |      Usuario    |
| CU-03  | Analizar una imagen             |      Usuario    |
| CU-04  | Detectar área de reconstrucción |      Sistema    |
| CU-05  | Reconstruir una imagen          |      Usuario    |
| CU-06  | Aumentar resolución             |      Usuario    |
| CU-07  | Comparar original y resultado   |      Usuario    |
| CU-08  | Descargar resultado individual  |      Usuario    |
| CU-09  | Descargar resultados en ZIP     |      Usuario    |
| CU-10  | Consultar historial             |      Usuario    |
| CU-11  | Consultar métricas              |      Usuario    |

-----------------------------------------------------------------------------------------------

# 5. Flujo general del sistema

```text
                    USUARIO
                       │
                       ▼
               ┌───────────────┐
               │ Cargar imagen │
               └───────┬───────┘
                       │
                       ▼
                ┌────────────┐
                │  Analizar  │
                └─────┬──────┘
                      │
                      ▼
             ┌─────────────────┐
             │  Detectar área  │
             │ de procesamiento│
             └────────┬────────┘
                      │
                      ▼
              ┌──────────────┐
              │  Reconstruir │
              └──────┬───────┘
                     │
                     ▼
             ┌─────────────────┐
             │     Mejorar     │
             │   resolución    │
             └────────┬────────┘
                      │
                      ▼
              ┌──────────────┐
              │   Comparar   │
              └──────┬───────┘
                     │
                     ▼
              ┌──────────────┐
              │   Descargar  │
              └──────────────┘
