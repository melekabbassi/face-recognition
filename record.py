# Recording a video using the webcam for 30 seconds and taking a picture every 5 seconds and saving it to a folder called \"Melek\"
# The video will be saved to a folder called \"Videos\"
# The video will be saved as \"Melek.mp4\"
# The pictures will be saved as \"Melek_1.jpg\", \"Melek_2.jpg\", \"Melek_3.jpg\", etc.

import cv2
import time
import os

# create a folder called "Melek" if it doesn't exist
if not os.path.exists("Melek"):
    os.makedirs("Melek")

# create a folder called "Videos" if it doesn't exist
if not os.path.exists("Videos"):
    os.makedirs("Videos")

# create a VideoCapture object
cap = cv2.VideoCapture(0)

# set the width and height of the video
cap.set(3, 640)
cap.set(4, 480)

# set the frame rate
frame_rate = 30

# set the number of seconds to record
num_seconds = 30

# set the number of seconds between each picture
picture_interval = 5

# set the number of pictures to take
num_pictures = num_seconds // picture_interval

# set the video codec
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

# set the video file name
video_file_name = "Videos/Melek.mp4"

# set the video file path
video_file_path = os.path.join(os.getcwd(), video_file_name)

# create a VideoWriter object
out = cv2.VideoWriter(video_file_path, fourcc, frame_rate, (640, 480))

# set the start time
start_time = time.time()

# set the current time
current_time = time.time()

# set the number of pictures taken
num_pictures_taken = 0

# loop until the number of seconds has passed
while current_time - start_time < num_seconds:
    
        # read the current frame
        ret, frame = cap.read()
    
        # write the current frame to the video file
        out.write(frame)
    
        # if the number of seconds has passed
        if current_time - start_time > num_pictures_taken * picture_interval:
    
            # set the picture file name
            picture_file_name = "Melek/Melek_" + str(num_pictures_taken + 1) + ".jpg"
    
            # set the picture file path
            picture_file_path = os.path.join(os.getcwd(), picture_file_name)
    
            # save the current frame as a picture
            cv2.imwrite(picture_file_path, frame)
    
            # increment the number of pictures taken
            num_pictures_taken += 1
    
        # update the current time
        current_time = time.time()

# release the VideoCapture object
cap.release()

# release the VideoWriter object
out.release()

# close all windows
cv2.destroyAllWindows()

# print a message
print("Done")