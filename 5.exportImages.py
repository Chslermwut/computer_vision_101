#read images
import cv2

#gray image 
img = cv2.imread('images/dog.jpg',0)
imageResize = cv2.resize(img,(500,500))
#show images
cv2.imshow("my dog",imageResize)

#export images
cv2.imwrite("images/Output.jpg",imageResize)



cv2.waitKey(0)
cv2.destroyAllWindows()
