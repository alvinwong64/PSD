import json
import os
from PIL import Image
import  shutil


from tqdm  import tqdm

def convert_json_to_yolo(parent_path):

    # os.makedirs(target_path, exist_ok=True)

    flags_dict = {}
    shape_dict = {}

    count_type_parking = {
        'occupied': 0,
        'vacant': 1,
        'unavailable': 2
    }

    # Walk through the root folder and its subfolders
    for folder_path, _, file_names in os.walk(parent_path):
        for filename in tqdm(file_names):

            if filename.endswith(".json"):
                file_path = os.path.join(folder_path, filename)
                image_path = os.path.join(folder_path.replace('json_labels','images'), os.path.splitext(filename)[0] + ".jpg")
                # os.makedirs(target_directory, exist_ok=True)


                # Load the JSON data from the file
                try:
                    with open(file_path, "r") as file:
                        data = json.load(file)

                        flags_dict[filename] = [key for key, value in data["flags"].items() if value == True]

                        shape_dict[filename] = data["shapes"]

                        # Open the image file
                        image = Image.open(image_path)

                        # Get the dimensions (width and height) of the image
                        width, height = image.size

                        # print(f"Image width: {width}px")
                        # print(f"Image height: {height}px")


                        strng = ""
                        for lst in shape_dict[filename]:

                            str2 = lst['label'].lower().replace(' ', 't').replace('%', '').replace(':',';')
                            str2 = str2.split(';')

                            strng += str(count_type_parking[str2[0]])

                            lst1 = lst['points']
                            for points in lst1:
                                strng += f' {int(points[0])/width} {int(points[1])/height}'
                            strng += f'\n'
                        # print(strng)
                        save_label_path = os.path.join(parent_path, os.path.splitext(filename)[0] + ".txt")
                        # save_img_path = os.path.join(parent_path + r'\images', os.path.splitext(filename)[0] + ".jpg")
                        # shutil.copy(image_path, save_img_path)

                        with open(save_label_path, "w") as file:
                            file.write(strng)

                except Exception as e:
                    print(f"Error loading {file_path}: {str(e)}")
        # print(count_type)
        # print(count_type_parking)




# Directory containing JSON files
data_directory = r"D:\alvin\yolotrain\Yolo_self_collect\train\json_labels"

convert_json_to_yolo(data_directory)
