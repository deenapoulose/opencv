import cv2
import numpy as np
img=cv2.imread('cir.jpg',1)
image=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('img',image)
lower=np.array([110,50,50])
upper=np.array([130,252,250])
a=cv2.inRange(image,lower,upper)

cv2.imshow('image',a)
res=cv2.bitwise_and(img,img,mask=a)
cv2.imshow('res',res)
cv2.waitKey(10000)
cv2.destroyAllWindows()
