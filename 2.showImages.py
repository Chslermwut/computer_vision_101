# show images

# read
import cv2
img = cv2.imread('images/dog.jpg')

# show
cv2.imshow("dog images",img)
cv2.waitKey(delay=5000)   #show pic 5s and close
cv2.destroyAllWindows()   #send all resource to window