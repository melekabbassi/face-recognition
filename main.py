import face_recognition
import cv2
import os
import pickle

KNOWN_FACES_DIR = 'known_faces'
UNKNOWN_FACES_DIR = 'unknown_faces'
TOLERANCE = 0.5
FRAME_THICKNESS = 2
FONT_THICKNESS = 2
MODEL = 'hog'  # default: 'hog', other one can be 'cnn' - CUDA accelerated (if available) deep-learning pretrained model
# what is hog ?
# https://www.learnopencv.com/histogram-of-oriented-gradients/
# what is cnn ?
# https://www.learnopencv.com/understanding-convolution-neural-network/

print("loading known faces")

known_faces = []
known_names = []
matches = []

for name in os.listdir(KNOWN_FACES_DIR):
    for filename in os.listdir(f"{KNOWN_FACES_DIR}/{name}"):
        image = face_recognition.load_image_file(f"{KNOWN_FACES_DIR}/{name}/{filename}")
        encoding = face_recognition.face_encodings(image)[0]
        known_faces.append(encoding)
        known_names.append(name)

print("processing unknown faces")

for filename in os.listdir(UNKNOWN_FACES_DIR):
    print(filename)
    image = face_recognition.load_image_file(f"{UNKNOWN_FACES_DIR}/{filename}")
    locations = face_recognition.face_locations(image, model=MODEL)
    encodings = face_recognition.face_encodings(image, locations)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    for face_encoding, face_location in zip(encodings, locations):
        results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
        match = None
        if True in results:
            match = known_names[results.index(True)]
            print(f"Match found: {match}")
            
            top_left = (face_location[3], face_location[0])
            bottom_right = (face_location[1], face_location[2])
            color = [0, 255, 0]
            cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)

            top_left = (face_location[3], face_location[2])
            bottom_right = (face_location[1], face_location[2]+22)
            cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
            cv2.putText(image, match, (face_location[3]+10, face_location[2]+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 0, 200), FONT_THICKNESS)

            matches.append(match)
            pickle.dump(matches, open("matches.pkl", "wb"))

            # create a folder matched_faces if it doesn't exist already and save the matched faces in it
            # the name of the images should be numbers starting from 0            

            if not os.path.exists("matched_faces"):
                os.mkdir("matched_faces")
                cv2.imwrite(f"matched_faces/0.jpg", image)
            else:
                cv2.imwrite(f"matched_faces/{len(os.listdir('matched_faces'))}.jpg", image)

            # if not os.path.exists("matched_faces"):
            #     os.mkdir("matched_faces")
            # cv2.imwrite(f"matched_faces/{len(os.listdir('matched_faces'))}.jpg", image)

    cv2.imshow(filename, image)
    cv2.waitKey(0)
    cv2.destroyWindow(filename)  