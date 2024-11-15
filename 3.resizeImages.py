#resize

#read -> resize
import cv2
img = cv2.imread('images/dog.jpg')
imgResize = cv2.resize(img,(400,400))

#show
cv2.imshow("dog images",imgResize)
cv2.waitKey(0)
cv2.destroyAllWindows()


