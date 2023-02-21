from pathlib import Path

coverage_spectral_helper = [False]*59
coverage_spectral_helper_file = "./coverage_spectral_helper.txt"

coverage_boxplot = [False]*58
coverage_boxplot_file = "./coverage_boxplot.txt"

# Check that the test directories exist.
if not (Path(__file__).parent / 'baseline_images').exists():
    raise OSError(
        'The baseline image directory does not exist. '
        'This is most likely because the test data is not installed. '
        'You may need to install matplotlib from source to get the '
        'test data.')
