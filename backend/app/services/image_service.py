from pathlib import Path

from PIL import Image


ALLOWED_FORMATS = {"PNG", "JPEG", "WEBP", "BMP"}


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

        return {
            "filename": path.name,
            "format": image_format,
            "width": image.width,
            "height": image.height,
            "mode": image.mode,
        }