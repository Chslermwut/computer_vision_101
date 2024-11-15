# tell point(x,y) on mouse event
import cv2
img = cv2.imread('images/tree.jpg')

#function clickPosition 
# event -> mouse left , right
def clickPosition(event,x,y,flags,param):
  if event == cv2.EVENT_LBUTTONDOWN:
   
    text = str(x)+","+str(y)
    cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),2)
    cv2.imshow("tree picture",img)

#show image
cv2.imshow("tree picture",img)
#work with mouse
#setMouseCallback("tree picture",function)
cv2.setMouseCallback("tree picture",clickPosition)
cv2.waitKey(0)
cv2.destroyAllWindows()