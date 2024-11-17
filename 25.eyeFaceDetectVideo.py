import cv2

cap = cv2.VideoCapture('images/head.mp4')

#read file xml
face_cascade = cv2.CascadeClassifier('detect/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('detect/haarcascade_eye_tree_eyeglasses.xml')

while(cap.isOpened()):
  check ,frame = cap.read()
  if check == True :
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_detect = face_cascade.detectMultiScale(gray_frame,1.1,4)
    eye_detect = eye_cascade.detectMultiScale(gray_frame,1.1,4)

    for (fx,fy,fw,fh) in face_detect:
      cv2.rectangle(frame,(fx,fy),(fx+fw,fy+fh),(0,0,255),5)
      for (ex,ey,ew,eh) in eye_detect:
        cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(0,0,255),5)

    cv2.imshow("output",frame)
    if cv2.waitKey(2) & 0xFF == ord("e"):
      break
  else:
    break

cap.release()
cv2.destroyAllWindows()