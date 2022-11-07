import cv2
image = cv2.imread("Batman.jpg")

## Use the cvtColor() function to grayscale the image
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', grey_img)
cv2.waitKey(0) 

#convert Gray to Invert
invert = cv2.bitwise_not(grey_img)
cv2.imshow('Invert', invert)
cv2.waitKey(0) 

#convert to blur
blur = cv2.GaussianBlur(invert,(21,21),0)
cv2.imshow('Blur', blur)
cv2.waitKey(0) 

invertedblur = cv2.bitwise_not(blur)
cv2.imshow('invertedblur', invertedblur)
cv2.waitKey(0) 

sketch = cv2.divide(grey_img , invertedblur,scale=256.0)
cv2.imshow('Sketch', sketch)
cv2.waitKey(0) 

cv2.imwrite("Sketch2.png",sketch)

cv2.destroyAllWindows()