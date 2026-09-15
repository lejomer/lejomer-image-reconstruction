from fastapi import FastAPI

from api.routes_health import router as health_router


app = FastAPI(
    title="LEJOMER — Reconstrucción de Imágenes",
    description="API para procesamiento y reconstrucción de imágenes autorizadas.",
    version="0.1.0"
)


app.include_router(
    health_router,
    prefix="/api/v1"
)