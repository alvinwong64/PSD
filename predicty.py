from ultralytics import YOLO
import os
import cv2
# from PIL import Image

# Load model
model = YOLO(r'D:\alvin\yolov8\run\segment\ps20_mod\PS20_RCCv2_4head2\weights\best.pt')

# Run inference
test_dir =r"D:\alvin\yolotrain\ps2.0\test\images"

results = model.predict(source=test_dir,device=0,save=True ,overlap_mask=False, agnostic_nms=True, iou=0.4, conf=0.5,stream=True)

for r in results:
    # print(r.path)
    label_path = r.path.replace('images','labels').replace('jpg','txt')

    with open(label_path, "r") as file:  
        lsx = []
        lsy = []
        lines = file.readlines()
        if lines:
            for line in lines:
                line = line.split()
                lsx.append([float(x) * 256 for x in line[1::2]])
                lsy.append([float(x) * 512 for x in line[2::2]])
            print(lsx,lsy)

    print(r.boxes)
    if r.boxes.data is not None and len(r.boxes.data) > 0:
        for data in r.boxes.data:
            # print(data)
            x1, y1, x2, y2 = data[0:4]

for filename in os.listdir(test_dir):

    if filename.endswith('.jpg'):  # Make sure it's a text file
        file_path = os.path.join(test_dir, filename)
        label_path = os.path.join(test_dir.replace('images','labels'), os.path.splitext(filename)[0] + ".txt")
        print(file_path)


        
        with open(label_path, "r") as file:  
            lines = file.readlines()

            for line in lines:
                line = line.split()
                print(line)
                strng = ""
                # # a.add(int(line[0]))
                # for x,y  in zip(line[1::2],line[2::2]):
                #     strng += f'{line[0]} {int(x)/width} {int(y)/height}'

                




                


# # # Visualize the results on the frame
# annotated_frame = results[0].plot()
# save_path = test_dir.replace('.jpg','_test1.jpg')

# cv2.imwrite(save_path,annotated_frame)

