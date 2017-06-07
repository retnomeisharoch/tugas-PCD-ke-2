import cv2 #memanggil library opencv
import numpy as np #memanggil library numpy
import matplotlib.pyplot as plt #memanggil library matplotlib

img=cv2.imread('ty.jpg')

gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img=cv2.GaussianBlur(gray,(3,3),0)

laplacian=cv2.Laplacian(img, cv2.CV_64F)
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

plt.subplot(2,2,1),plt.imshow(img,cmap='gray'),plt.title('Gambar Asli')
plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap='gray'),plt.title('Laplacian')
plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap='gray'),plt.title('Sobel X')
plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap='gray'),plt.title('Sobel Y')
plt.xticks([]), plt.yticks([])

plt.show()