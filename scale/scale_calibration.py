import cv2
import numpy as np


def calibrate_scale_bar(image: 'cv2.Mat') -> float:
    """Calculate the real-world distance per pixel using a drawn scale bar.

    The user draws a horizontal line over the scale bar on ``image`` and then
    inputs the real length of that bar in micrometers. The function returns the
    micrometers-per-pixel ratio.

    Parameters
    ----------
    image : cv2.Mat
        Image containing a scale bar.

    Returns
    -------
    float
        Real-world distance represented by a single pixel in micrometers.
    """

    if image is None:
        raise ValueError("Invalid image for calibration")

    draw = {'pts': []}

    def _mouse(event: int, x: int, y: int, flags: int, param) -> None:
        if event == cv2.EVENT_LBUTTONDOWN:
            draw['pts'] = [(x, y)]
        elif event == cv2.EVENT_LBUTTONUP and draw['pts']:
            draw['pts'].append((x, y))
            cv2.line(image, draw['pts'][0], draw['pts'][1], (0, 255, 0), 2)
            cv2.imshow("Scale", image)

    cv2.imshow("Scale", image)
    cv2.setMouseCallback("Scale", _mouse)
    cv2.waitKey(0)
    cv2.destroyWindow("Scale")

    if len(draw['pts']) != 2:
        raise RuntimeError("Scale bar was not drawn correctly")

    (x1, _), (x2, _) = draw['pts']
    num_pixels = abs(x2 - x1)
    real_length = float(input("Enter the real length of the scale bar in micrometers: "))
    return real_length / num_pixels
