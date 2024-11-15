import cv2

img = cv2.imread("images/dog.jpg")

#drawing line
# line(ภาพ , จุดเริ่มต้น (x,y) , จุดสุดท้าย(x,y) , สี (BGR) , ความหนา)
# arrowedLine ลูกศร
cv2.line(img ,(0,0),(100,100),(255,0,0),5)
cv2.arrowedLine(img ,(200,200),(300,300),(0,255,0),5)
cv2.imshow("picture",img)

cv2.waitKey(0)
cv2.destroyAllWindows()