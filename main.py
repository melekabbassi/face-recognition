import cv2
import face_recognition

image = cv2.imread('Haaland.jpg')
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_encoding = face_recognition.face_encodings(rgb)[0]

cv2.imshow('image', image)

cv2.waitKey(0)