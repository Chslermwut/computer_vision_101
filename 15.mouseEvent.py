# tell point(x,y) on mouse event
import cv2
img = cv2.imread('images/tree.jpg')

#show image
cv2.imshow("tree picture",img)
cv2.waitKey(0)
cv2.destroyAllWindows()