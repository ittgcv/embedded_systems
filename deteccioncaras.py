import cv2
# Load the cascade
face_cascade = cv2.CascadeClassifier('face_detector.xml')
# Read the input image
img = cv2.imread('caras.jpeg')
# Detect faces
faces = face_cascade.detectMultiScale(img, 1.1, 4)
# Draw rectangle around the faces
print(len(faces))
for (x, y, w, h) in faces: 
  cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
# Export the result
cv2.imwrite("face_detected.png", img) 
print('Successfully saved')
