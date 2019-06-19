import cv2
from PIL import Image
from numpy import array, uint8
import math     		
def findball() :
	img = cv2.imread("camImage.png",1)
	cv2.namedWindow("HSV Image",cv2.WINDOW_NORMAL)
	cv2.namedWindow("Binary Image",cv2.WINDOW_NORMAL)
	cv2.namedWindow("dilate Image",cv2.WINDOW_NORMAL)
	cv2.namedWindow("Ball detected Image",cv2.WINDOW_NORMAL)
	print "Width of the image :" + str(img.shape[1]) #width
	print "Height of the image :" + str(img.shape[0]) #hight
	hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	cv2.imshow("HSV Image", hsv)
	red = cv2.inRange(hsv,array([0,100,100],uint8),array([25,255,255],uint8))
	cv2.imshow("Binary Image", red)
	erode = cv2.erode(red,None,iterations = 1)
	dilate = cv2.dilate(erode,None,iterations = 5)
	cv2.imshow("dilate Image", dilate)
	contours,hierarchy = cv2.findContours(dilate,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
	print "Y-axis : Top to bottom"
	print "X-axis : Left to right"
	Cx,Cy,W,H,X,Y=0,0,0,0,0,0 
	maxdiag=0
	for cnt in contours:
	    x,y,w,h = cv2.boundingRect(cnt)
	    cx,cy = x+w/2, y+h/2
	    print "Center : ("+ str(cx)+","+str(cy)+") , Width :"+str(w)+", Height :"+str(h)+", Radius = (Width+Height)/2 : "+str((w+h)/2)
	    cv2.rectangle(img,(x,y),(x+w,y+h),[0,255,255],2)
	    if (math.sqrt(w*w+h*h)>maxdiag) :
			maxdiag=math.sqrt(w*w+h*h)
			Cx,Cy,W,H,X,Y=cx,cy,w,h,x,y
	cv2.rectangle(img,(X,Y),(X+W,Y+H),[0,23,255],2)
	print "CENTER : ("+ str(Cx)+","+str(Cy)+") , WIDTH :"+str(W)+", HEIGHT :"+str(H)
	cv2.imshow('Ball detected Image',img)
	front = 0
	if (Cy<130):
		print "move one step in front"
		front =1
	if (Cx>135 and Cx<160): 
	    print "Move right to adjust"
	    return [0,front]
	elif Cx > 225:
		return [5,front]
	elif (Cx>160 and Cx<185): 
		print "Move left to adjust"
		return [1,front]
	elif Cx < 95 :
		return [4,front]
	elif Cx<160:
		return [2,front] 	 #   Kick using LEFT Foot
	elif Cx>160:
		return [3,front]    #    nKick using RIGHT Foot



