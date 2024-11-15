import cv2

img = cv2.imread("images/dog.jpg")

imgResize = cv2.resize(img,(700,700))

#regtangle
#regtangle(ภาพ,มุม1(บนซ้าย) , มุม2 (ล่างขวา) ,สี(BGR) , ความหนา)
#ความหนา -1 ระบายสี
cv2.rectangle(imgResize,(0,0),(100,100),(0,0,255),-1)

cv2.imshow("output",imgResize)
cv2.waitKey(0)
cv2.destroyAllWindows()