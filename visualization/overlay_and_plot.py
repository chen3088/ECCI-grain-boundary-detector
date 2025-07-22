import cv2
import matplotlib.pyplot as plt
import pandas as pd


def show_result(edge_image: 'cv2.Mat', results: pd.DataFrame) -> None:
    """Overlay edges on the original image and display analysis results.

    Parameters
    ----------
    edge_image : cv2.Mat
        Binary edge image.
    results : pandas.DataFrame
        DataFrame produced by :func:`analysis.line_intersection.analyze_grain_size`.
    """
    overlay = cv2.cvtColor(edge_image, cv2.COLOR_GRAY2BGR)
    overlay[edge_image > 0] = [0, 0, 255]

    plt.figure(figsize=(8, 8))
    plt.imshow(overlay[..., ::-1])
    plt.title("Detected Grain Boundaries")
    plt.axis("off")
    plt.show()

    print(results)
