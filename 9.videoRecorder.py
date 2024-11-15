# video record
import cv2
#open webcam and make sure frame
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

#setting video for save mp4
# XVID --> .AVI
fourcc = cv2.VideoWriter_fourcc(*'MP4V')

# save video (ชื่อ,fourcc,frame rate , ขนาด video)
result = cv2.VideoWriter("images/output.mp4", fourcc, 20.0, (640, 480))

while (cap.isOpened()):
  check, frame = cap.read()

  cv2.imshow("webcam", frame)
  result.write(frame)
  if cv2.waitKey(1) & 0xFF == ord("e"):
      break

result.release()
cap.release()
cv2.destroyAllWindows()
