# ECCI-grain-boundary-detector
This is a opencv-based tool for determination of grain size in SEM-ECCI image

## Usage

1. Install required Python packages:

```bash
pip install opencv-python numpy matplotlib scikit-image
```

2. Launch Jupyter Notebook and open the provided notebook:

```bash
jupyter notebook "automatic grain detector.ipynb"
```

3. Follow the instructions in the notebook to:
   - Crop the region of interest from your SEM image.
   - Tune preprocessing parameters to enhance grain boundaries.
   - Save the overlay of detected edges.

The repository includes a sample image (`10000xbse_007.tif`) that can be used to try the notebook.
