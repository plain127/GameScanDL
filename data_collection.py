import cv2
import os

video_path = "{Input mp4 video address}"
output_dir = "./data/{gamename}"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

video = cv2.VideoCapture(video_path)

cnt = 9057

while video.isOpened():
    ret, image = video.read()
    if not ret:
        break
    
    frame_number = int(video.get(cv2.CAP_PROP_POS_FRAMES))

    if frame_number % 300 == 0:
        frame_path = os.path.join(output_dir, f"mabinogiframe{cnt}.jpg")
        cv2.imwrite(frame_path, image)
        cnt += 1

video.release()