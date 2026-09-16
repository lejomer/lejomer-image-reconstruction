from pathlib import Path

import pytest
from PIL import Image

from backend.app.services.image_service import validate_image


def test_validate_image():
    test_image = Path("backend/tests/test_image.png")

    Image.new("RGB", (100, 80), "white").save(test_image)

    result = validate_image(str(test_image))

    assert result["filename"] == "test_image.png"
    assert result["format"] == "PNG"
    assert result["width"] == 100
    assert result["height"] == 80
    assert result["mode"] == "RGB"

    test_image.unlink()


def test_image_too_small():
    test_image = Path("backend/tests/test_small.png")

    Image.new("RGB", (32, 32), "white").save(test_image)

    with pytest.raises(ValueError, match="Imagen demasiado pequeña"):
        validate_image(str(test_image))

    test_image.unlink()


def test_file_not_found():
    test_image = "backend/tests/no_existe.png"

    with pytest.raises(FileNotFoundError, match="No existe el archivo"):
        validate_image(test_image)