import cv2
import numpy as np

img = cv2.imread("resources/lena.png")
kernel = np.ones((5,5), np.uint8)			# queremos que todos los valores de la matriz sean 1,  tamaño de la matriz es 5x5

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # imagen original a gris
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)   # difuminacion de imagen
imgCanny= cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1) # dilatacion de linea = Cambia el grosor de la linea de canny (aumento)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1) # erocion de linea = Cambia el grosor de la linea de canny (disminuye)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(10000)