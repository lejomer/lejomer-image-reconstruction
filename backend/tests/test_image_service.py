from pathlib import Path

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