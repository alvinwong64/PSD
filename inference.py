from ultralytics import YOLO
import os
import time
import cv2
from tqdm import tqdm




# Load model
model = YOLO(r'D:\alvin\yolov8\run\segment\PSD_MOD\PSD_Norm_yolov9\weights\best.pt')

# Run inference
test_dir =r"D:\alvin\yolotrain\Yolo_self_collect\test\images"
result= model.predict(test_dir, device=0,stream=True)
for r in result:
    print(r.speed)
# t_time=0
# count =0
# for item in tqdm(os.listdir(test_dir)):
#     item_path = os.path.join(test_dir, item)
#     if os.path.isfile(item_path) and item.endswith(".jpg"):
#         count+=1

#         start_time = time.time()
#         results = model(item_path,verbose=False)
#         t_time += (time.time() - start_time)

#         # # Visualize the results on the frame
#         # annotated_frame = results[0].plot()
#         # save_path = item_path.replace('.jpg','_test.jpg')
        
#         # cv2.imwrite(save_path,annotated_frame)

# fps = count/(t_time)
# ms = 1/ fps
# print(fps,ms)



