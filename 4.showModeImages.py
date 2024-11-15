#read images
import cv2

# read mode number
# 0 = gray
# 1 = color
# -1 = alpha channel
img = cv2.imread("images/dog.jpg",-1)
print(img)

#show images
cv2.imshow("dog images",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

