import cv2
import numpy as np

cheque = cv2.imread('K:\\Papers\\Signature Matching\\Dataset\\1_Cheque\\1.jpg',cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(cheque,cv2.COLOR_BGR2HSV)

lower_black = np.array([20,140,50])
upper_black = np.array([255,210,150])

mask = cv2.inRange(hsv,lower_black,upper_black)
res = cv2.bitwise_and(cheque,cheque,mask=mask)

cv2.imshow('Image',cheque)
cv2.imshow('Mask',mask)
cv2.imshow('Result',res)
cv2.waitKey()
cv2.destroyAllWindows()
