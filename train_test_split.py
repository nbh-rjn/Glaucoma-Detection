import os
import shutil
from natsort import natsorted

# Define the paths
source_dir_images = "images"
train_dir_images = "train_images"
test_dir_images = "test_images"

source_dir_masks_cups = "cups"
train_dir_masks_cups = "train_masks_cups"
test_dir_masks_cups = "test_masks_cups"

source_dir_masks_discs = "discs"
train_dir_masks_discs = "train_masks_discs"
test_dir_masks_discs = "test_masks_discs"

# Create the train and test directories if they don't exist
os.makedirs(train_dir_images, exist_ok=True)
os.makedirs(test_dir_images, exist_ok=True)

os.makedirs(train_dir_masks_cups, exist_ok=True)
os.makedirs(test_dir_masks_cups, exist_ok=True)

os.makedirs(train_dir_masks_discs, exist_ok=True)
os.makedirs(test_dir_masks_discs, exist_ok=True)

# Get a list of all files in the source directory
files_images = os.listdir(source_dir_images)
files_masks_cups = os.listdir(source_dir_masks_cups)
files_masks_discs = os.listdir(source_dir_masks_discs)

# Sort the file names using natural sorting
files_images = natsorted(files_images)
files_masks_cups = natsorted(files_masks_cups)
files_masks_discs = natsorted(files_masks_discs)

# Split the files into train and test sets
train_files_images = files_images[:80]
test_files_images = files_images[80:]

train_files_masks_cups = files_masks_cups[:80]
test_files_masks_cups = files_masks_cups[80:]

train_files_masks_discs = files_masks_discs[:80]
test_files_masks_discs = files_masks_discs[80:]

# Copy the train files to the train directory
for file in train_files_images:
    src_path = os.path.join(source_dir_images, file)
    dst_path = os.path.join(train_dir_images, file)
    shutil.copy(src_path, dst_path)

for file in train_files_masks_cups:
    src_path = os.path.join(source_dir_masks_cups, file)
    dst_path = os.path.join(train_dir_masks_cups, file)
    shutil.copy(src_path, dst_path)

for file in train_files_masks_discs:
    src_path = os.path.join(source_dir_masks_discs, file)
    dst_path = os.path.join(train_dir_masks_discs, file)
    shutil.copy(src_path, dst_path)

# Copy the test files to the test directory
for file in test_files_images:
    src_path = os.path.join(source_dir_images, file)
    dst_path = os.path.join(test_dir_images, file)
    shutil.copy(src_path, dst_path)

for file in test_files_masks_cups:
    src_path = os.path.join(source_dir_masks_cups, file)
    dst_path = os.path.join(test_dir_masks_cups, file)
    shutil.copy(src_path, dst_path)

for file in test_files_masks_discs:
    src_path = os.path.join(source_dir_masks_discs, file)
    dst_path = os.path.join(test_dir_masks_discs, file)
    shutil.copy(src_path, dst_path)

print("Files copied successfully.")
