from ultralytics import YOLO
import torch
import random
import argparse





if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--wdir', type=str, default=None, help='dir name')
    parser.add_argument('--data', type=str, default='psd.yaml', help='datafolder')
    parser.add_argument('--epochs', type=int, default=300, help='epochnum')
    parser.add_argument('--model', type=str, default='yolov8n-seg.yaml', help='epochnum')

    args = parser.parse_args()
    

    # print(torch.cuda.is_available())
    torch.cuda.set_device(0)

    # Load a model (without load original .pt file, so the performance not good)
    # no transfer
    # model = YOLO(r'D:\alvin\ultralytics\ultralytics\cfg\models\v8\yolov8-seg.yaml')

    model = YOLO(args.model)
    # print("$$$$$$$$$$$$$$")

    # model = YOLO('yolov8n-seg.pt')  # load an official model
    # model = YOLO(r'D:\alvin\ultralytics\runs\segment\PSD_RCCv2_4head3\weights\last.pt')  # load a custom model

# Validate the model
    # metrics = model.val()
    # print(metrics)
    # if args.wdir != None:
    with torch.autocast("cuda"): 
        results = model.train(data=args.data, epochs=args.epochs, device=0 , name=args.wdir, overlap_mask=False, verbose=True,amp=False, batch=8)
    # else:
        # results = model.train(data=args.data, epochs=args.epochs, seed=random.randint(1, 100000),device=0)
