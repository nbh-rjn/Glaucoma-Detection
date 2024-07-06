import os
import shutil
from natsort import natsorted

# Define the paths

test_dir_masks_cups = "output_cups"
test_dir_masks_discs = "output_discs"


# Get a list of all files in the source directory
files_masks_cups = os.listdir(test_dir_masks_cups)
files_masks_discs = os.listdir(test_dir_masks_discs)

# Sort the file names using natural sorting
files_masks_cups = natsorted(files_masks_cups)
files_masks_discs = natsorted(files_masks_discs)

from PIL import Image


# Function to calculate the number of white pixels in an image
def count_white_pixels(image_path):
    img = Image.open(image_path)
    img = img.convert("L")  # Convert to grayscale
    white_pixels = sum(
        1 for pixel in img.getdata() if pixel == 255)  # Count white pixels (assuming white is represented by 255)
    total_pixels = img.size[0] * img.size[1]  # Total number of pixels
    return white_pixels, total_pixels

i = 0
# Calculate the number of white pixels and output the ratio for each set of cup and disc
for cup, disc in zip(files_masks_cups, files_masks_discs):
    i += 1
    cup_path = os.path.join(test_dir_masks_cups, cup)
    disc_path = os.path.join(test_dir_masks_discs, disc)

    # Calculate white pixels for cup
    cup_white_pixels, cup_total_pixels = count_white_pixels(cup_path)

    # Calculate white pixels for disc
    disc_white_pixels, disc_total_pixels = count_white_pixels(disc_path)

    # Calculate ratio
    ratio = cup_white_pixels / disc_white_pixels

    print(f"Image {i} = {ratio}", end="")
    if ratio > 0.5:
        print(" - GLAUCOMA", end="")

    print(" ")
