#eye detection
import cv2

img = cv2.imread("images/eye.jpeg")
img = cv2.resize(img,(500,500))
#read file classcification
eye_cascade = cv2.CascadeClassifier("detect/haarcascade_eye_tree_eyeglasses.xml")

#change gray picture
gray_img =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#detect eye
scaleFactor = 1.2
minNeighbors = 4
eye_detect = eye_cascade.detectMultiScale(gray_img,scaleFactor,minNeighbors)

# show eye position
for (x,y,w,h) in eye_detect:
  cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
  

cv2.imshow("Original",img)
# cv2.imshow("Result",gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()