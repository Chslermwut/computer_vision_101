import cv2
import matplotlib.pyplot as plt

img = cv2.imread('images/gradient.jpg')
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#128(threshold) เก็บที่ thresh  , ภาพเก็บที่ result
thresh ,result1 = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY)
thresh ,result2 = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY_INV)
thresh ,result3 = cv2.threshold(gray_img,128,255,cv2.THRESH_TRUNC)
thresh ,result4 = cv2.threshold(gray_img,128,255,cv2.THRESH_TOZERO)
thresh ,result5 = cv2.threshold(gray_img,128,255,cv2.THRESH_TOZERO_INV)

# cv2.imshow("Output",gray_img)
# cv2.imshow("BINARY1",result1)
# cv2.imshow("BINARY2",result2)
# cv2.imshow("BINARY3",result3)
# cv2.imshow("BINARY4",result4)
# cv2.imshow("BINARY5",result5)
images = [gray_img,result1,result2,result3,result4,result5]
title = ["Output","BINARY1","BINARY2","BINARY3","BINARY4","BINARY5"]

for i in range(len(images)) :
  plt.subplot(2,3,i+1)
  plt.imshow(images[i])
  plt.title(title[i])
  plt.xticks([]),plt.yticks([])

plt.show()

# cv2.waitKey(0)
# cv2.destroyAllWindows()