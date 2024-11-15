import cv2

cap = cv2.VideoCapture("images/chaplin.mp4")

#read file classcification
eye_cascade = cv2.CascadeClassifier("detect/haarcascade_eye_tree_eyeglasses.xml")

while (cap.isOpened()):
  check , frame = cap.read()
  if check == True:
    gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #detect eye
    eye_detect = eye_cascade.detectMultiScale(gray_img,scaleFactor=1.2,minNeighbors=3)
    # show eye position
    for (x,y,w,h) in eye_detect:
      cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)
      cv2.imshow("Output",frame)
    if cv2.waitKey(1) & 0xFF == ord("e"):
      break
  else:
    break

cap.release()
cv2.destroyAllWindows()