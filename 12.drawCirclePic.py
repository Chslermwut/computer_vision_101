import cv2

img = cv2.imread('images/dog.jpg')

#circle
#circle(ภาพม,จุดศูนยฺกลาง(x,y),รัศมี , สี , ความหนา)

cv2.circle(img,(200,200),50,(0,255,20),5)

cv2.imshow("my dog" ,img)
cv2.waitKey(0)
cv2.destroyAllWindows()