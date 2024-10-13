import os
import json
from tqdm import tqdm

main_dir = r"D:\alvin\yolotrain\Yolo_self_collect\main_data"

for folder_path, _, file_names in os.walk(main_dir):

    for filename in tqdm(file_names):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)

            with open(file_path, 'r') as file:
                data = json.load(file)

            shape_dict = data["shapes"]

            for lst in shape_dict:
                str2 = lst['label'].lower().replace(' ', 't').replace('%', '').replace(':', ';')
                str2 = str2.split(';')[0]
                lst["label"]=str2

            # Write the modified data back to the file
            with open(file_path, 'w') as file:
                json.dump(data, file,indent=2)


