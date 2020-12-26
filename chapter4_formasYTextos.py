import cv2
import numpy as np 

img = np.zeros((512,512,3), np.uint8)
print(img.shape)

cv2.line(img, (0,0), (300,300), (0,255,0),3)
# cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0,255,0),3)  Linea de extremo a extremo
cv2.rectangle(img, (0,0), (250,350), (0,0,255), 2) # Dibuja rectangulo
cv2.rectangle(img, (0,0), (250,350), (0,0,255), cv2.FILLED) # Dibuja y llena rectangulo
cv2.circle(img,(400,50), 30, (255,255,0), 5)  # Dibuja circulo
cv2.putText(img, " OPENCV ", (300,200), cv2.FONT_HERSHEY_COMPLEX, 1, (0,150,0),3) #Pone texto en imagen



cv2.imshow("Image", img)
cv2.waitKey(3000)