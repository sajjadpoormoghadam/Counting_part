import cv2 
import matplotlib.pyplot as plt 
import numpy as np 

r_triangle = 0
b_triangle = 0
g_triangle = 0

r_quadangle = 0
b_quadangle = 0
g_quadangle = 0

r_circule = 0
b_circule = 0
g_circule = 0

img = cv2.imread("projects/Counting_part/images/shape_color1.png")
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img  , cv2.COLOR_BGR2HSV)

red_lower = np.array([136, 87, 111], np.uint8) 
red_upper = np.array([180, 255, 255], np.uint8) 
red_mask = cv2.inRange(hsv, red_lower, red_upper) 

green_lower = np.array([35, 80, 50] ,np.uint8)
green_upper = np.array([85, 255, 255], np.uint8)
green_mask = cv2.inRange(hsv, green_lower, green_upper) 

blue_lower = np.array([94, 80, 2], np.uint8) 
blue_upper = np.array([120, 255, 255], np.uint8) 
blue_mask = cv2.inRange(hsv, blue_lower, blue_upper)
kernel = np.ones((5,5) , "uint8")

red_mask = cv2.dilate(red_mask , kernel=kernel)
# res_red = cv2.bitwise_and(img , img , mask=red_mask)

blue_mask = cv2.dilate(blue_mask , kernel)
# res_blue = cv2.bitwise_and(img , img , mask= blue_mask)

green_mask = cv2.dilate(green_mask , kernel=kernel)
# res_green = cv2.bitwise_and(img , img , mask=green_mask)

contours , _ = cv2.findContours(red_mask , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)

for i , contour in enumerate(contours):

    approx = cv2.approxPolyDP(contour , 0.03 * cv2.arcLength(contour , True) , True)

    side = len(approx)
    if side == 3 :
        r_triangle +=1  
        label = "triangle "
    elif side == 4 :
        r_quadangle +=1
        label = "qaudangle "
    else :
        r_circule+=1
        label = "circule "
    area = cv2.contourArea(contour)
    if area > 200:
        x , y , w , h = cv2.boundingRect(contour)
        img = cv2.rectangle(img  , (x, y), (x+w , y+h) , (0,0,0) , 1 )

        cv2.putText(img , label + "Red", (x, y - 5),cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0, 0, 255))


contours , _ = cv2.findContours(blue_mask , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)

for i , contour in enumerate(contours):
    approx = cv2.approxPolyDP(contour , 0.03 * cv2.arcLength(contour , True) , True)

    side = len(approx)
    if side == 3 : 
        b_triangle +=1  
        label = "triangle "
    elif side == 4 :
        b_quadangle +=1  
        label = "qaudangle "
    else :
        b_circule +=1  
        label = "circule "
    area = cv2.contourArea(contour)
    if area > 200:
        x , y , w , h = cv2.boundingRect(contour)
        img = cv2.rectangle(img  , (x, y), (x+w , y+h) , (0,0,0) ,1 )

        cv2.putText(img , label + "Blue", (x, y - 5),cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255, 0, 0))



contours , _ = cv2.findContours(green_mask , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)

for i , contour in enumerate(contours):
    approx = cv2.approxPolyDP(contour , 0.02 * cv2.arcLength(contour , True) , True)

    side = len(approx)
    if side == 3 : 
        g_triangle +=1  
        label = "triangle "
    elif side == 4 :
        g_quadangle +=1
        label = "qaudangle "
    else :
        g_circule+= 1
        label = "circule "    
    area = cv2.contourArea(contour)
    if area > 200:
        x , y , w , h = cv2.boundingRect(contour)
        img = cv2.rectangle(img  , (x, y), (x+w , y+h) , (0,0,0) , 1 )

        cv2.putText(img , label + "Green", (x, y - 5),cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0, 255, 0))

print("red triangle :" , r_triangle)
print("red circule :" , r_circule)
print("red quadangle :" , r_quadangle)

print("blue triangle :" , b_triangle)
print("blue circule :" , b_circule)
print("blue quadangle :" , b_quadangle)

print("green triangle :" , g_triangle)
print("green circule :" , g_circule)
print("green quadangle :" , g_quadangle)


cv2.imshow("shape and color" , img)
cv2.waitKey(0)
cv2.destroyAllWindows()