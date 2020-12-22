import cv2

img = cv2.imread("resources/lena.png")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # imagen original a gris
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)   # difuminacion de imagen

cv2.imshow("Gray Image", imgGray)
cv2.imshow("blur Image", imgBlur)
cv2.waitKey(10000)