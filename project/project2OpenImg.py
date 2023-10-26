import cv2

image = cv2.imread('me.jpg')

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('output.jpg', image)
