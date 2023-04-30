import os
import cv2
import shutil
import numpy as np
from tqdm import tqdm
from datetime import datetime

def is_transparent(image):
    if image.ndim < 3:
        return False
    if image.shape[2] == 4:
        alpha_channel = image[:, :, 3]
        return alpha_channel.min() < 255
    return False

def find_matching_background(imgArr, threshold, target_rgb, tolerance_rgb):
    if imgArr.ndim < 3:
        return False

    diff_with_target = np.abs(imgArr[..., :3].astype(np.int16) - target_rgb)

    matching_mask = np.all(diff_with_target <= tolerance_rgb, axis=-1)
    percent = matching_mask.sum() / (imgArr.shape[0] * imgArr.shape[1])

    if percent >= threshold:
        return True
    else:
        return False

def main():
    # Define variables
    images_dir = 'images'
    parent_output_folder = 'sorted-images'
    matching_folder = 'matching-background'
    transparent_folder = 'transparent-background'
    photo_folder = 'photo'
    matching_threshold = 0.2
    target_rgb = (255, 255, 255)  # Change this to your desired color
    tolerance_rgb = (5, 5, 5)

    os.makedirs(os.path.join(parent_output_folder, matching_folder), exist_ok=True)
    os.makedirs(os.path.join(parent_output_folder, transparent_folder), exist_ok=True)
    os.makedirs(os.path.join(parent_output_folder, photo_folder), exist_ok=True)

    filenames = [f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.png', '.jpeg', '.webp'))]

    log_file = open("sorted_images_log.txt", "a")
    log_file.write(f"\n==================== New Run: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ====================\n")

    for filename in tqdm(filenames, desc="Processing images"):
        file_path = os.path.join(images_dir, filename)
        image = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)

        if is_transparent(image):
            shutil.copy(file_path, os.path.join(parent_output_folder, transparent_folder, filename))
            log_file.write(f"{filename}: Moved to {transparent_folder}\n")
        elif find_matching_background(image, matching_threshold, target_rgb, tolerance_rgb):
            shutil.copy(file_path, os.path.join(parent_output_folder, matching_folder, filename))
            log_file.write(f"{filename}: Moved to {matching_folder}\n")
        else:
            shutil.copy(file_path, os.path.join(parent_output_folder, photo_folder, filename))
            log_file.write(f"{filename}: Moved to {photo_folder}\n")

    log_file.close()

if __name__ == '__main__':
    main()