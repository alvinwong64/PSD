import sys
sys.path.append('D:\alvin\miou_yolov8') 
# from miou_yolov8 import ultralytics

from ultralytics import YOLO
import os
import cv2
from tqdm import tqdm
import pandas as pd

# dict1 = {"number of storage arrays": 45, "number of ports":2390}

if __name__ == '__main__':
    main_dir = r"D:\alvin\yolov8\run\segment\PSD_MOD"
    files= "best.pt"
    df_out = pd.DataFrame() 
    check=False
    for folder_path, dirs, file_names in os.walk(main_dir):


        for filename in file_names:

            if filename == files:
                check=True
                file_path = os.path.join(folder_path, filename)
                print(file_path)
                model = YOLO(file_path)

                # print(folder_path)
                # print(dirs)
                # print(file_names)


                results = model.val(data="psd.yaml" ,device=0, iou=0.5)
                r_dict = results.results_dict
                df = pd.DataFrame(data=r_dict, index=[folder_path])
                # print(df_out)

                df_out =pd.concat([df_out, df],axis=0)

    if check:
        result_path = os.path.join(main_dir, 'output.xlsx')
        with pd.ExcelWriter(result_path) as writer:
            df_out.to_excel(writer, index=True , header=True)

    # print(results.results_dict)


