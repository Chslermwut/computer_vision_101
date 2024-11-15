#connect point
import cv2
import numpy

img = numpy.zeros([500,500,3])

points = []

def clickPosition(event,x,y,flags,param):
  if event == cv2.EVENT_LBUTTONDOWN:
    cv2.circle(img,(x,y),10,(0,255,0),2)
    #append การต่อจุด x,y
    points.append((x,y))
    #นับจุดมากกว่า 2
    if len(points)>=2:
      #จุดต้นไปจุดปลาย แต่ -2 -1 จะกลับกัน
      cv2.line(img,points[-2],points[-1],(0,0,255),2)
    cv2.imshow("Output",img)

cv2.imshow("Output",img)

cv2.setMouseCallback("Output",clickPosition)
cv2.waitKey(0)
cv2.destroyAllWindows()