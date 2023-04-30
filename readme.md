# Background Sorter Script

This script sorts the images in a folder into different categories based on image background. It checks if an image has a transparent or matching color background (within a given tolerance) and sorts them accordingly. Remaining images are considered as photos with non-matching background colors.

## Dependencies

To use this script, you need to install the following packages:

1. OpenCV (cv2): for reading and processing the images
2. numpy: for dealing with array manipulations
3. tqdm: for displaying progress bars

You can install these packages using pip: `pip install opencv-python numpy tqdm`


## How to Use

1. Place your images in a folder named 'images' within the same directory as the script.
2. Update the following variables in the script according to your needs:
    - `images_dir`: Name of the folder containing the images
    - `parent_output_folder`: Name of the parent output folder where sorted images will be stored
    - `matching_folder`: Name of the folder for images with matching background color
    - `transparent_folder`: Name of the folder for images with a transparent background
    - `photo_folder`: Name of the folder for images with non-matching background color
    - `matching_threshold`: Minimum percentage of matching background pixels to consider an image as matching
    - `target_rgb`: Tuple containing the target background color (RGB values) you want to match
    - `tolerance_rgb`: Allows some variation in the matching background color. For example, if target_rgb is (230, 230, 230) and tolerance_rgb is (10, 10, 10), any pixel with an RGB value within the range (R: 225-235, G: 225-235, B: 225-235) will be considered a match.
3. Run the script by executing the command `python sort-photos.py`
4. You will find the sorted images in the specified output folders.

## Notes

The script creates a log file `sorted_images_log.txt` with details about the sorting process, indicating the folder in which each image was moved. Each new run of the script appends a new log entry in the same file.