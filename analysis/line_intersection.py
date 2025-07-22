import numpy as np
import pandas as pd


def analyze_grain_size(edge_image: 'cv2.Mat', microns_per_pixel: float) -> pd.DataFrame:
    """Estimate grain size using random line intersections.

    This is a simplified implementation that draws random horizontal and
    vertical lines on the binary ``edge_image`` and counts the number of
    intersections with grain boundaries. The results are returned as a
    ``pandas.DataFrame`` with the line index and intersection count.

    Parameters
    ----------
    edge_image : cv2.Mat
        Binary image with grain boundary edges.
    microns_per_pixel : float
        Real-world distance per pixel used to convert results.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing line indices and intersection counts.
    """
    import cv2  # imported here to avoid dependency if not used elsewhere

    if edge_image is None:
        raise ValueError("Edge image is required")

    height, width = edge_image.shape[:2]
    num_lines = 10
    rng = np.random.default_rng()
    data = []

    for idx in range(num_lines):
        y = rng.integers(0, height)
        line = edge_image[y, :]
        transitions = np.count_nonzero(line[1:] > line[:-1])
        data.append({"line": idx, "intersections": int(transitions)})

    df = pd.DataFrame(data)
    df["estimated_grain_size"] = (width / df["intersections"]).replace([np.inf, np.nan], 0) * microns_per_pixel
    return df
