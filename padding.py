import os
from PIL import Image


def add_padding(image_path):
    img = Image.open(image_path)
    width, height = img.size

    # Check if the image size matches the desired size
    if width == 1376 and height == 1371:
        return  # Image already has the correct size

    print(image_path)
    # Calculate padding parameters
    left_padding = (1376 - width) // 2
    top_padding = (1371 - height) // 2
    right_padding = 1376 - width - left_padding
    bottom_padding = 1371 - height - top_padding

    # Apply padding
    padded_img = Image.new(img.mode, (1376, 1371), color='black')  # Create a white canvas
    padded_img.paste(img, (left_padding, top_padding))  # Paste the original image onto the canvas with padding

    # Save the padded image
    padded_img.save(image_path)


def process_images_in_folder(folder_path):
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".png"):  # Assuming images are in PNG format
            image_path = os.path.join(folder_path, filename)
            add_padding(image_path)
            #print(f"Processed: {filename}")


# Specify the folder containing the images
folder_path = "train_images"

# Process images in the folder
process_images_in_folder(folder_path)
