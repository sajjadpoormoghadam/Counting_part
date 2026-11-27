import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

triangle =0
quadrangle = 0
circule = 0

img = cv2.imread("projects/Counting_part/images/shape_detect.png")

gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

_ , threshold = cv2.threshold(gray , 127 , 255 ,cv2.THRESH_BINARY)
contours , _ = cv2.findContours(threshold ,cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)

for i , contour in enumerate(contours):
    if i == 0 :
        continue 

    approx = cv2.approxPolyDP(contour , 0.02 *cv2.arcLength(contour , True) , True)

    sides = len(approx)

    cv2.drawContours(img , [contour] , 0 , (255 , 0, 0) , 3)

    M = cv2.moments(contour)
    if M["m00"] != 0:
        x =int( M["m10"] / M["m00"])
        y = int(M["m01"] / M["m00"])

    if sides == 3:
        triangle += 1
        label = "Triangle"
    if sides == 4 : 
        quadrangle += 1
        label = "Quadrangle"
    if sides > 4 : 
        circule+=1 
        label = "Circule"

    cv2.putText(img , label , (x,y) , cv2.FONT_HERSHEY_SIMPLEX , 0.6 , (255,255,255) , 3)

print("circule: " , str(circule))
print("Triangle: " , str(triangle))
print("Qaudangle: " , str(quadrangle))

cv2.imshow("shape",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


