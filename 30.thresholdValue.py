#compare Threshold and Matplotlib
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('images/ant.jpg')
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

thres_value = [50,100,130,200,230]
plt.subplot(231,xticks=[],yticks=[])
plt.title("Original")
plt.imshow(gray_img,cmap="gray")

for i in range(len(thres_value)):
  thresh ,result = cv2.threshold(gray_img,thres_value[i],255,cv2.THRESH_BINARY)
  plt.subplot(232+i)
  plt.title("%d"%thres_value[i])
  plt.imshow(result,cmap="gray")
  plt.xticks([]),plt.yticks([])

plt.show()


# cv2.imshow("Output",gray_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()