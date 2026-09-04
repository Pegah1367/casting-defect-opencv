import numpy as np

from src.average_blur import apply_average_blur


def test_average_blur_keeps_shape():
    image = np.zeros((100, 100), dtype=np.uint8)

    result = apply_average_blur(image, (5, 5))

    assert result.shape == image.shape


def test_average_blur_changes_pixel_values():
    image = np.zeros((5, 5), dtype=np.uint8)
    image[2, 2] = 255

    result = apply_average_blur(image, (3, 3))

    assert 0 < result[2, 2] < 255
