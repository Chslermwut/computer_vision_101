#create trackBar (color palate)
import cv2
#numpy as = set name
import numpy as np

#np set dark   //zeros = dark((size,BGR),pic 8 bit)
img = np.zeros((200,250,3),np.uint8)

#create name window Trackbar
cv2.namedWindow("Color Trackbar")

def display(value):
  pass

#begin craete Trackbar   // Trackbar name,Window name,begin value,count is max [min-max] , onChange
cv2.createTrackbar("B","Color Trackbar",0,255,display)
cv2.createTrackbar("G","Color Trackbar",0,255,display)
cv2.createTrackbar("R","Color Trackbar",0,255,display)

while True:
  cv2.imshow("Color Trackbar",img)
  if cv2.waitKey(1) & 0xFF == ord("e"):
    break

  #get color from Trackbar
  blue=cv2.getTrackbarPos("B","Color Trackbar")
  green=cv2.getTrackbarPos("G","Color Trackbar")
  red=cv2.getTrackbarPos("R","Color Trackbar")

  #add array start to finish is array 3 dimension
  img[:] = [blue,green,red]

cv2.destroyAllWindows()


