import cv2
import time
from ultralytics import YOLO
from tqdm import tqdm

def main():
    acc_fps = []
    
    video_path = r"D:\alvin\yolotrain\Yolo_self_collect\0926.mpeg"
    cap = cv2.VideoCapture(video_path)
    original_fps = cap.get(cv2.CAP_PROP_FPS)  # Get original video FPS

    # Check if video is opened successfully
    if not cap.isOpened():
        print("Error: Failed to open video.")
        return

    # Get total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # used to record the time when we processed last frame 
    prev_frame_time = time.time()

    # Load YOLO model
    model = YOLO(r"D:\alvin\yolov8\run\segment\PSD_MOD\PSD_RCCv2_4head\weights\best.pt")

    # Get frame width and height
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    size = (frame_width, frame_height) 

    # Define output video parameters
    output_video_path = 'filename_conf055.avi'
    codec = cv2.VideoWriter_fourcc(*'MJPG')

    # Initialize VideoWriter object for writing the output video
    saver = cv2.VideoWriter(output_video_path, codec, original_fps, size)  # Set FPS to original FPS
    
    with tqdm(total=total_frames) as pbar:
        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                break

            results = model(frame, conf=0.6, verbose=False, stream=True)

            for result in results:
                new_frame_time = time.time()
                divisor = new_frame_time - prev_frame_time
                if divisor == 0:
                    divisor = 0.005
                fps = 1 / divisor

                acc_fps.append(fps)
                leng = min(20, len(acc_fps))
                avg_fps = sum(acc_fps[-20:]) / leng

                cv2.putText(frame, f'FPS: {avg_fps:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                annotated_frame = result.plot()

                # Write frame to video
                saver.write(annotated_frame) 
                prev_frame_time = time.time()
                pbar.update(1)

    cap.release()
    saver.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
