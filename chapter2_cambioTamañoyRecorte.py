import cv2

img = cv2.imread("Resources/lambo.png")
print(img.shape) # tamaño de la imagen

imgResize = cv2.resize(img,(300, 200)) # redimencionamos la imagen con 300 de ancho y 200 de alto
print(imgResize.shape)

imgCropped = img[0:200, 200:500]

cv2.imshow("Image", img)
cv2.imshow("Image resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(3000)