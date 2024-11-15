#open video
import cv2

cap = cv2.VideoCapture("images/chaplin.mp4")

while (cap.isOpened()):
    check , frame = cap.read()
    # ไปถึง frame สุดท้ายจะ error คือ video อ่านไปครบ frame แล้วต้องใส่เงื้อนไขด้านล่าง
    if check == True:
        cv2.imshow("video",frame)
        if cv2.waitKey(1) & 0xFF == ord("e"):   
         # video จะไวมากเนื้องจาก waitKey 1 ms
          break
    # ถ้าจบ video frame สุดท้ายก็ให้ break ออกไปด้วย
    else :
      break

cap.release()
cv2.destroyAllWindows()