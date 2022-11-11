import cv2
import face_recognition

image1 = cv2.imread('images/Haaland.jpg')
rgb1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
image1_encoding = face_recognition.face_encodings(rgb1)[0]

image2 = cv2.imread('images/Haaland3.png')
rgb2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
image2_encoding = face_recognition.face_encodings(rgb2)[0]

result = face_recognition.compare_faces([image1_encoding], image2_encoding)

print(result)

cv2.waitKey(0)
# aaa