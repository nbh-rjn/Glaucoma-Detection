"""
in this file im using the original dataset's "masks"
to separate the masks for cups and discs
and place them in relevant folders
named with corresponding numbers
"""


import cv2
import os

# Directory containing the images
images_dir = "masks"

# Get a list of all files in the directory
image_files = os.listdir(images_dir)

i = 1
# Iterate over each image file
for image_file in image_files:
    # Construct the full path to the image
    image_path = os.path.join(images_dir, image_file)

    # Load the image using OpenCV
    img = cv2.imread(image_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # cups
    _, threshold_img_cup = cv2.threshold(gray_img, 128, 0, cv2.THRESH_TOZERO_INV)

    # discs
    _, threshold_img_disc_1 = cv2.threshold(gray_img, 128, 0, cv2.THRESH_TOZERO_INV)
    _, threshold_img_disc_2 = cv2.threshold(threshold_img_disc_1, 0, 255, cv2.THRESH_BINARY)

    # Check if the image is loaded successfully
    if img is not None:
        #cups
        processed_image_path = os.path.join("cups", f"{i}.tif")
        cv2.imwrite(processed_image_path, threshold_img_cup)

        processed_image_path = os.path.join("discs", f"{i}.tif")
        cv2.imwrite(processed_image_path, threshold_img_disc_2)
        i += 1
    else:
        print(f"Error loading image: {image_file}")
