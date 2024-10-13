# from PIL import Image, ImageDraw
import os
from tqdm import tqdm
import json

dir = r"D:\alvin\yolotrain\Yolo_self_collect\main_data\test\json_labels"
from tqdm import tqdm


def load_json_files_in_folder_and_subfolders(root_folder):
    data_dict = {}
    flags_dict = {}
    shape_dict = {}
    labels_dict = {}
    count_type = {'slanted': 0,
                  'perpendicular': 0,
                  'parallel': 0,
                  'non_park': 0,

                  }
    count_type_parking = {
        'occupied': 0,
        'vacant': 0,
        'unavailable': 0
    }

    # Walk through the root folder and its subfolders
    for folder_path, _, file_names in os.walk(root_folder):
        for filename in tqdm(file_names):
            # Check if the file is a JSON file
            if filename.endswith(".json"):
                file_path = os.path.join(folder_path, filename)

                # Load the JSON data from the file
                try:
                    with open(file_path, "r") as file:
                        data = json.load(file)
                        # Store the data in a dictionary with the file path as the key
                        data_dict[filename] = data
                        flags_dict[filename] = [key for key, value in data["flags"].items() if value == True]

                        shape_dict[filename] = data["shapes"]
                        # labels_dict[filename] = data
                        # print(labels_dict[filename])
                        # print(len(shape_dict[filename]))
                        count_type[flags_dict[filename][0]] += (1 * len(shape_dict[filename]))
                        # print(count_type)

                        for lst in shape_dict[filename]:
                            # lst['label'].
                            # for item in lbl:
                            # str = lst['label'].split(';')[0].lower()
                            str2 = lst['label'].lower().replace(' ', '').replace('%','')
                            # print(str2)
                            count_type_parking.setdefault(str2, 0)
                            # count_type_parking[str] += 1
                            count_type_parking[str2] += 1

                except Exception as e:
                    print(f"Error loading {file_path}: {str(e)}")
        # print(count_type)
        # print(count_type_parking)

    return data_dict, flags_dict, shape_dict, count_type_parking, count_type


data, flags, shape, count_1, count_2 = load_json_files_in_folder_and_subfolders(dir)
# print(data)
# print(flags)
# print(shape)
all_values = [item for value_list in shape.values() for item in value_list]
# print(all_values)
print(sorted(count_1.items()), sorted(count_2.items()))
# print(count_2)

# Now 'loaded_data' is a dictionary where keys are file paths to JSON files,
# and values are the loaded JSON data from those files.
# You can access individual JSON files like this:
# json_data = loaded_data['path/to/subfolder/example.json']
