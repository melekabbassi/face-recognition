# record a video for 30 seconds and take a picture every 5 seconds and save it to the known_faces/{name} folder based on the user input
# the video will be deleted after the pictures are taken
# import the necessary packages

import cv2
import time
import os

# ask the user for the name
name = input("Enter your name: ")

# create the known_faces directory if it does not exist
if not os.path.exists("known_faces"):
    os.makedirs("known_faces")
    
# create a folder for the user if it doesn't exist
if not os.path.exists(f"known_faces/{name}"):
    os.makedirs(f"known_faces/{name}")

# delete the video if it exists
if os.path.exists("face.mp4"):
    os.remove("face.mp4")

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
video_file_name = "face.mp4"

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
        
        # display the current frame
        cv2.imshow("frame", frame)
        
        # set the current time
        current_time = time.time()
        
        # check to see if it is time to take a picture
        if current_time - start_time >= picture_interval * num_pictures_taken:
            
            # set the picture file name
            picture_file_name = f"known_faces/{name}/{name}_{num_pictures_taken}.jpg"
            
            # set the picture file path
            picture_file_path = os.path.join(os.getcwd(), picture_file_name)
            
            # write the current frame to the picture file
            cv2.imwrite(picture_file_path, frame)
            
            # increment the number of pictures taken
            num_pictures_taken += 1
            
        # check to see if the "q" key was pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

# release the VideoCapture object
cap.release()

# release the VideoWriter object
out.release()

# close all open windows
cv2.destroyAllWindows()

# delete the video file
os.remove("face.mp4")