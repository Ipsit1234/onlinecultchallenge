import cv2
import numpy as np
import turtle
from scipy import ndimage
img = cv2.imread('spidey1.png')
img = ndimage.rotate(img,90)
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img = cv2.Canny(img,100,200)
contours,hierarchy = cv2.findContours(img,1,2)
t1 = turtle.Turtle()
t1.pencolor('black')
t1.speed(0)
turtle.bgcolor('red')
for i in range(len(contours)):
    for j in range(len(contours[i])):
        if j == 0:
            t1.pu()
            t1.goto(contours[i][j][0][1]-img.shape[1]/2,img.shape[0]/2-contours[i][j][0][0])
        else:
            t1.pd()
            t1.goto(contours[i][j][0][1]-img.shape[1]/2,img.shape[0]/2-contours[i][j][0][0])
t1.ht()
turtle.exitonclick()
