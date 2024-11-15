#show pixel color from picture
import cv2
import numpy

img = cv2.imread('images/candy.jpg')

def clickPosition(event,x,y,flags,param):
  if event == cv2.EVENT_LBUTTONDOWN:
    # 0 = blue , 1 = green , 2 = red
    blue = img[y,x,0]
    green = img[y,x,1]
    red = img[y,x,2]
    # text = str(blue)+","+str(green)+","+str(red)
    # cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2)

    # create new picture  numpy.zeros = สีดำ  จอทั้งหมดเป็นสีดำ
    imgColor = numpy.zeros([300,300,3],numpy.uint8)
    # กำหนด สีใหม่  [:] เลือก pixel ทั้งหมดทุกแถว ทุกคอลัมน์
    imgColor[:] = [blue,green,red]
    cv2.imshow("Result",imgColor)

cv2.imshow("Output",img)
cv2.setMouseCallback("Output",clickPosition)
cv2.waitKey(0)
cv2.destroyAllWindows()