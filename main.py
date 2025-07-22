from crop.crop_tool import mouse_crop
from scale.scale_calibration import calibrate_scale_bar
from preprocessing.enhance_edges import preprocess_image
from analysis.line_intersection import analyze_grain_size
from visualization.overlay_and_plot import show_result
from config import image_path


def main() -> None:
    """Run the grain size analysis pipeline."""
    cropped_image = mouse_crop(str(image_path))
    microns_per_pixel = calibrate_scale_bar(cropped_image)
    edges = preprocess_image(cropped_image)
    results_df = analyze_grain_size(edges, microns_per_pixel)
    show_result(edges, results_df)


if __name__ == "__main__":
    main()
