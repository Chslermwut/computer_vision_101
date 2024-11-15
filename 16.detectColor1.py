#detect color
import cv2

img = cv2.imread('images/candy.jpg')

def clickPosition(event,x,y,flags,param):
  if event == cv2.EVENT_LBUTTONDOWN:
    blue = img[y,x,0]
    green = img[y,x,1]
    red = img[y,x,2]

    text = str(blue)+","+str(green)+","+str(red)
    cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2)
    cv2.imshow("color detect",img)

cv2.imshow('color detect',img)
cv2.setMouseCallback("color detect" ,clickPosition)
cv2.waitKey(0)
cv2.destroyAllWindows()