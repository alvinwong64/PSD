from PIL import Image
import os
import numpy as np

def get_number_of_channels(image):
    # Convert the image to a NumPy array
    img_array = np.array(image)
    # Return the number of channels
    return img_array.shape[-1]

def find_images_with_channel_count(folder_path, target_channels):
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            try:
                img = Image.open(file_path)
                num_channels = get_number_of_channels(img)
                # print(f"{file_name} has {num_channels} channels")
                if num_channels == target_channels:
                    print(f"{file_name} has {target_channels} channels")
            except Exception as e:
                print(f"Error processing {file_name}: {e}")

# Replace 'path_to_your_folder' with the actual path to your folder containing images
folder_path = r'D:\alvin\yolotrain\SNU\train\images'
# Specify the target number of channels
target_channels = 1  # Change this to 3 for RGB images
find_images_with_channel_count(folder_path, target_channels)
