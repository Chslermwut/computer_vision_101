# face detection
import cv2

img = cv2.imread("images/boy.jpg")
img = cv2.resize(img,(500,500))
#read file classcification
face_cascade = cv2.CascadeClassifier("detect/haarcascade_frontalface_default.xml")

#change gray picture
gray_img =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#detect face
scaleFactor = 1.2
minNeighbors = 4
face_detect = face_cascade.detectMultiScale(gray_img,scaleFactor,minNeighbors)

# show face position
for (x,y,w,h) in face_detect:
  cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
  

cv2.imshow("Original",img)
# cv2.imshow("Result",gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()