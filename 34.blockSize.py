#adaptive threshold
import cv2
import matplotlib.pyplot as plt

#gray image = 0
img = cv2.imread('images/map.jpg',0)
size_img = cv2.resize(img,(500,400))

#Block Size
size = [3,5,9,17,33]

#show image 2 row 3 col
#231 = 2 row 3 col 1 begin start
plt.subplot(231,xticks=[],yticks=[])
plt.imshow(size_img,cmap="gray")

for i in range(len(size)):
  result = cv2.adaptiveThreshold(size_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,size[i],1)
  plt.subplot(232+i)
  plt.title("%d"%size[i])
  plt.imshow(result,cmap="gray")
  plt.xticks([]),plt.yticks([])

plt.show()


  
