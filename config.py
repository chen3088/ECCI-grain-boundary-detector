"""Project configuration parameters."""

from pathlib import Path

# Path to the default image used for analysis
image_path: Path = Path("10000xbse_007.tif")

# Default preprocessing parameters
initial_clahe_clip_limit: float = 2.0
initial_clahe_tile_grid_size: int = 8
gaussian_blur_size: int = 5
median_blur_size: int = 5
final_clahe_clip_limit: float = 2.0
final_clahe_tile_grid_size: int = 8
low_threshold: int = 50
high_threshold: int = 150
