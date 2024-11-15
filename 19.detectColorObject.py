import cv2
import numpy

while (True):
    img = cv2.imread('images/ball.jpeg')  # Read the image
    img = cv2.resize(img, (700, 400))     # Resize the image

    # Set the color range for detecting the object in BGR (Blue, Green, Red)
    upper = numpy.array([10, 19, 174])    # Upper bound of the color range (darker/stronger color)
    lower = numpy.array([100, 126, 255])  # Lower bound of the color range (lighter/weak color)

    # Create a mask based on the color range
    mask = cv2.inRange(img, upper, lower)

    # Apply the mask to extract the object of the specified color
    result = cv2.bitwise_and(img, img, mask=mask)

    # Check if the user pressed the 'e' key to exit the loop
    if cv2.waitKey(1) & 0xFF == ord("e"):
        break
    
    # Display the original image, the mask, and the result (the detected color)
    cv2.imshow("Original", img)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)

cv2.destroyAllWindows()
