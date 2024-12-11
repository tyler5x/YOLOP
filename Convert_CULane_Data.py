# Create binary segmentation masks for lane lines from (x,y) key point coordinates. This is necessary to allow YOLOP, which expects binary mask labels, to run
# on the CULane dataset, which only has (x,y) line coordinates as a txt file.

import os
from PIL import Image
import numpy as np
import cv2

# directory = '05181432_0203.MP4'
directory = 'drivable_masks3/val'
# abs_directory = '/gpfs/accounts/eecs542f24_class_root/eecs542f24_class/amixan/ankhoros/homework1/homework4/YOLOP/CULane/driver_37_30frame/05181432_0203.MP4'
abs_directory = '/gpfs/accounts/eecs542f24_class_root/eecs542f24_class/amixan/ankhoros/homework1/homework4/YOLOP/CULane/driver_37_30frame/drivable_masks3/val'

# save_directory = 'masks'
# save_directory = '/gpfs/accounts/eecs542f24_class_root/eecs542f24_class/amixan/ankhoros/homework1/homework4/YOLOP/CULane/driver_37_30frame/images2/val'
save_directory = '/gpfs/accounts/eecs542f24_class_root/eecs542f24_class/amixan/ankhoros/homework1/homework4/YOLOP/CULane/driver_37_30frame/drivable_masks4/val'

#Resolution of CULane images: Width: 1640, Height: 590

# List to store the width and height of all images
widths = []
heights = []
line_counts = []
images_names = []
txt_names = []
txt_files = []
image_files = []

image_size=(1640, 590)

def read_splines_from_file(file_path):
    splines = []
    line_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            line_count += 1
            points = list(map(float, line.split()))
            spline = [(points[i], points[i+1]) for i in range(0, len(points), 2)]
            splines.append(spline)

        line_counts.append(line_count)

    return splines

def create_lane_mask(file_path):
    # Create a black image
    img = np.zeros((image_size[1], image_size[0]), dtype=np.uint8)

    # Read the spline data from the text file
    splines = read_splines_from_file(file_path)

    # Draw each spline as a white line on the black image
    for spline in splines:
        points = np.array(spline, dtype=np.int32)
        points = points.reshape((-1, 1, 2))  # Reshape to match OpenCV's polyline format
        cv2.polylines(img, [points], isClosed=False, color=255, thickness=5)
    return img


# Loop through all files in the directory
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    # Only process image files (you can expand the conditions for other formats)
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        images_names.append(filename)
    elif filename.lower().endswith(('.txt')):
        txt_names.append(filename)

txt_names.sort()
images_names.sort()
print(images_names)

# Generate resized original images

for file_name in images_names:
    file_path = os.path.join(directory, file_name)
    print(file_name)
    print(file_path)
    with Image.open(file_path) as img:
        # Get the dimensions of the image
        width, height = img.size
        widths.append(width)

        heights.append(height)
        name = img.filename
        save_dir = os.path.join(save_directory, file_name)
        img2 = img.resize((1280, 720))
        img2.save(save_dir)
        print(save_dir)

# Generate masks

# for file_name in txt_names:
#     file_path = os.path.join(abs_directory, file_name)
#     print(file_path)
#     mask = create_lane_mask(file_path)

#     first_split = os.path.splitext(file_name)[0]
#     mask_filename = os.path.splitext(first_split)[0] + '.png'
#     mask_filepath = os.path.join(save_directory, mask_filename)
#     cv2.imwrite(mask_filepath, mask)
#     print(f"Mask saved as {mask_filename}")