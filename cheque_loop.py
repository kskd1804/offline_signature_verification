import cv2
import numpy as np
import math
import tensorflow as tf

input = cv2.imread('K:\\Papers\\Signature Matching\\Dataset\\1_Cheque\\4.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imwrite("K:\\Papers\\Signature Matching\\Dataset\\grayscale.jpg",input);
cheque = cv2.imread('K:\\Papers\\Signature Matching\\Dataset\\grayscale.jpg',cv2.IMREAD_COLOR);

height, width, _ = cheque.shape;
min_x=0
min_y=0
flag = 0
max_x = 0
max_y = 0
count=0
for i in range(math.floor(height/2),height):
    for j in range(math.floor(width*(2/3)),width):
        if((cheque[i,j]<=[80,80,80]).all()):
            if flag==0:
                flag=1
                min_x = j
                min_y = i
                max_x=j
                max_y=i
            else:
                if min_x > j: min_x = j
                if max_x < j: max_x = j
                if min_y > i: min_y = i
                if max_y < i: max_y = i
            if max_x<j: max_x=j
            if max_y<i:max_y=i
            count = 0
        else:
            if flag==1:
                if count > 900: break
                count+=1

target = cheque[min_y-5:max_y+5,min_x-5:max_x+5]
#cv2.rectangle(cheque,(min_x-5,min_y-5),(max_x+5,max_y+5),(0,0,255),1)
#cv2.imwrite('K:\\Papers\\Signature Matching\\Dataset\\target.jpg',target)
cv2.imshow('INPUT',cheque)
cv2.imshow('TARGET',target)
cv2.waitKey(0)
cv2.destroyAllWindows()
