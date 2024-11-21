#adaptive threshold
import cv2

#gray image = 0
img = cv2.imread('images/map.jpg',0)
size_img = cv2.resize(img,(500,400))

thresh,th1=cv2.threshold(size_img,128,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(size_img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,1)
th3 = cv2.adaptiveThreshold(size_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,1)

cv2.imshow("THREH",th1)
cv2.imshow("MEAN",th2)
cv2.imshow("GAUSSIAN",th3)

cv2.waitKey(0)
cv2.destroyAllWindows()