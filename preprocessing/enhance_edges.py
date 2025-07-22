import cv2
import numpy as np


def preprocess_image(
    image: 'cv2.Mat',
    clip_limit: float = 2.0,
    tile_grid_size: int = 8,
    gaussian_size: int = 5,
    median_size: int = 5,
    low_threshold: int = 50,
    high_threshold: int = 150,
) -> 'cv2.Mat':
    """Enhance edges in ``image`` using CLAHE, blurs and Canny detection.

    Parameters
    ----------
    image : cv2.Mat
        Grayscale or BGR image to process.
    clip_limit : float, optional
        CLAHE clip limit, by default 2.0.
    tile_grid_size : int, optional
        Tile grid size for CLAHE, by default 8.
    gaussian_size : int, optional
        Kernel size for Gaussian blur, by default 5.
    median_size : int, optional
        Kernel size for median blur, by default 5.
    low_threshold : int, optional
        Lower threshold for Canny, by default 50.
    high_threshold : int, optional
        Upper threshold for Canny, by default 150.

    Returns
    -------
    cv2.Mat
        Binary edge image from Canny detector.
    """

    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image.copy()

    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=(tile_grid_size, tile_grid_size))
    clahe_img = clahe.apply(gray)

    if gaussian_size % 2 == 0:
        gaussian_size += 1
    blurred = cv2.GaussianBlur(clahe_img, (gaussian_size, gaussian_size), 0)

    if median_size % 2 == 0:
        median_size += 1
    median_blur = cv2.medianBlur(blurred, median_size)

    final_clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=(tile_grid_size, tile_grid_size))
    final_img = final_clahe.apply(median_blur)

    edges = cv2.Canny(final_img, low_threshold, high_threshold)
    return edges
