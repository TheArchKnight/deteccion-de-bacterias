import cv2 as cv2
import numpy as np

img = cv2.cvtColor(cv2.imread("res/dataset-master/dataset-master/JPEGImages/BloodImage_00130.jpg"), cv2.COLOR_BGR2RGB)
img_HSV = cv2.cvtColor(cv2.imread("res/dataset-master/dataset-master/JPEGImages/BloodImage_00130.jpg"), cv2.COLOR_BGR2HSV)
lower_blue = np.array([53,58,188])
upper_blue = np.array([159,171,255])
mask = cv2.inRange(img_HSV, lower_blue, upper_blue)
res = cv2.bitwise_and(img,img, mask= mask)
cv2.imshow('Imagen', res)
cv2.waitKey(0)
