from pathlib import Path

from PIL import Image


ALLOWED_FORMATS = {"PNG", "JPEG", "WEBP", "BMP"}

MIN_WIDTH = 64
MIN_HEIGHT = 64

MAX_WIDTH = 10000
MAX_HEIGHT = 10000


def validate_image(image_path: str) -> dict:
    """
    Valida una imagen y obtiene información básica.

    La función no modifica la imagen.
    """

    path = Path(image_path)

    if not path.exists():
        raise FileNotFoundError(f"No existe el archivo: {image_path}")

    with Image.open(path) as image:
        image_format = image.format

        if image_format not in ALLOWED_FORMATS:
            raise ValueError(
                f"Formato no permitido: {image_format}"
            )

        if image.width < MIN_WIDTH or image.height < MIN_HEIGHT:
            raise ValueError(
                f"Imagen demasiado pequeña. "
                f"Dimensiones mínimas: {MIN_WIDTH}x{MIN_HEIGHT} píxeles."
            )

        if image.width > MAX_WIDTH or image.height > MAX_HEIGHT:
            raise ValueError(
                f"Imagen demasiado grande. "
                f"Dimensiones máximas: {MAX_WIDTH}x{MAX_HEIGHT} píxeles."
            )

        return {
            "filename": path.name,
            "format": image_format,
            "width": image.width,
            "height": image.height,
            "mode": image.mode,
        }