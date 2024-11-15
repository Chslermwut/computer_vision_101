#open camera
import cv2

#open camera เลขคือจำนวนกล้อง ถ้ามีกล้องเดียวใส่ 0
cap = cv2.VideoCapture(0)

#open camera all time
while (True):
  ref , frame = cap.read() # ref เป็น boolean [เป็นตัวแปลอื่นได้ //check]  รับภาพ frame ต่อ frame
  cv2.imshow('video',frame)

  # waitKey loop ไม่ให้เกิดการค้าง  0 จะเป็นการหยุดไม่ให้ dela//ถ้าต้องการออกให้กด e 
  if cv2.waitKey(1) & 0xFF == ord("e"):
      break

# คืนทรัพยากรให้เครื่อง clear ram
cap.release()
cv2.destroyAllWindows()
