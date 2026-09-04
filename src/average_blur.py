import cv2


def apply_average_blur(image, kernel_size=(5, 5)):
    return cv2.blur(image, kernel_size)
