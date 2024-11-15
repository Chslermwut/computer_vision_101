import cv2

img = cv2.imread("images/dog.jpg")

#putText
#putText(ภาพ ,ข้อความ ,พิกัดแสดง (x,y),font, size, color, thinkness)
cv2.putText(img,"DOG",(10,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,100),2)
cv2.imshow("text picture" ,img)
cv2.waitKey(0)
cv2.destroyAllWindows()