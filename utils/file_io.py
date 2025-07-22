from pathlib import Path
from typing import Union
import cv2


def get_filename(path: Union[str, Path]) -> str:
    """Return the filename without its directory from ``path``."""
    return Path(path).name


def save_images(directory: Union[str, Path], name: str, **images) -> None:
    """Save ``images`` to ``directory`` with ``name`` as prefix.

    Parameters
    ----------
    directory : str or Path
        Location where images will be saved.
    name : str
        Prefix for saved image files.
    images : dict
        Mapping of suffix to image array to save.
    """
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    for suffix, img in images.items():
        filename = directory / f"{name}_{suffix}.tif"
        cv2.imwrite(str(filename), img)
