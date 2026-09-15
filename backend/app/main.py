from fastapi import FastAPI

app = FastAPI(
    title="LEJOMER — Reconstrucción de Imágenes",
    description="API para procesamiento y reconstrucción de imágenes autorizadas.",
    version="0.1.0"
)


@app.get("/api/v1/health")
def health_check():
    return {
        "status": "ok",
        "project": "LEJOMER — Reconstrucción de Imágenes",
        "version": "0.1.0"
    }