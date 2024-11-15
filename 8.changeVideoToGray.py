# change video to gray scale
import cv2

cap = cv2.VideoCapture("images/chaplin.mp4")

while (cap.isOpened()):
  check , frame = cap.read()

  if check == True:
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("video",gray)
    if cv2.waitKey(10) & 0xFF == ord("e"):
      break
  else :
    break

cap.release()
cv2.destroyAllWindows()
