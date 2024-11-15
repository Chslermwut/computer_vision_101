#show Datetime on Video/Webcam
import cv2
import datetime

#read video // webcam
# cap = cv2.VideoCapture("images/chaplin.mp4")
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
  check ,frame = cap.read()

  if check == True:
    #show putText,DateTime
    currectTime = str(datetime.datetime.now())
    cv2.putText(frame,currectTime,(80,50),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)
    cv2.imshow("video",frame)
    if cv2.waitKey(1) & 0xFF == ord("e"):
      break
  
  # else :
  #   break

cap.release()
cv2.destroyAllWindows()