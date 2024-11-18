#matplotlib show images
import cv2

#matplotlib pyploy
import matplotlib.pyplot as plt

img = cv2.imread("images/girl.jpg")
imgResize = cv2.resize(img,(600,450))

#cv2 show BGR
cv2.imshow("Output",imgResize)

#image to RGB
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)  

#matplotlib RGB
plt.imshow(img)
plt.show()