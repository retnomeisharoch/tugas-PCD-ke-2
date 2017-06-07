import numpy as np #memanggil library numpy
import cv2 #memanggil library opencv
import matplotlib.pyplot as plt #memanggil library pyplot

img=cv2.imread('ty.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('ty', img)
hist=cv2.calcHist([img],[0],None,[256],[0,256])

plt.hist(img.ravel(),256,[0,256])
plt.title('Histogram for gray scale picture')
plt.show()

