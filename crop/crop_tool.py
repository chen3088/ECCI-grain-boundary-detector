import cv2
from typing import Tuple


def mouse_crop(image_path: str) -> 'cv2.Mat':
    """Interactively crop a region of interest from an image.

    The function displays the image located at ``image_path`` and lets the
    user select a rectangular region with the mouse. The ROI is returned as an
    OpenCV image array.

    Parameters
    ----------
    image_path : str
        Path to the input image file.

    Returns
    -------
    cv2.Mat
        Cropped image chosen by the user.
    """
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Image not found at {image_path}")

    roi = cv2.selectROI("Image", image, showCrosshair=True)
    x, y, w, h = roi
    cropped = image[int(y) : int(y + h), int(x) : int(x + w)]
    cv2.destroyWindow("Image")
    return cropped
