import numpy as np
import math 
import matplotlib.pyplot as plt
#from cv2.cv import *
from PIL import Image
from tempfile import TemporaryFile
from numpy import linalg as LA
import numpy as np
import cv2
from cv2.cv import *

#def ShortestPath(Graph,Source)
#This code is only valid for obstacles which have small obstacles and it just gives a cost function anyway
im = cv2.imread('/home/pulkit/Desktop/4_1_map.jpg');
DistanceTransformmatrix = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
for i in range(1175):
    for j in range(0,1100):
        print i,j
        if (DistanceTransformmatrix[i,j]<=10):
            DistanceTransformmatrix[i,j]=0;
        else:
            DistanceTransformmatrix[i,j]=255;
#DistanceTransformmatrix[811:820,980:990] = 255;
#DistanceTransformmatrix[144:154,144:154] = 255;

		#print DistanceTransformmatrix[i,j]
#DistanceTransformmatrix = np.asarray(DistanceTransform);
NewDistanceTransformmatrix = np.zeros((1177,1102));
NewDistanceTransformmatrix[1:1176,1:1101]=DistanceTransformmatrix;
#NewDistanceTransformmatrix[811,1036] = 0;
#NewDistanceTransformmatrix[811:820,1036:1046] = 0;
#cv2.imwrite('/home/pulkit/Desktop/pathfinal.jpg',DistanceTransformmatrix);

#check Point1#print DistanceTransformmatrix
#print DistanceTransformmatrix

goalDistanceTransform = (1175*1100)*(np.ones((1177,1102),dtype='float64'))
goalDistanceTransform[811,1036] = 0
#1175 1100
values = np.zeros(5);
for i in range(2,1176):
	for j in range(2,1101):
         print i,j
         if(NewDistanceTransformmatrix[i,j] != 0):
        	values[0] =goalDistanceTransform[i,j];
        	values[1] =goalDistanceTransform[i-1,j]+1;
        	values[2] =goalDistanceTransform[i+1,j]+1;
        	values[3] =goalDistanceTransform[i,j-1]+1;
        	values[4] =goalDistanceTransform[i,j-1]+1;
        	goalDistanceTransform[i,j] = min(values)


        	#goalDistanceTransform[i,j] = min(values); 

for i in reversed(range(0,1174)):
	for j in reversed(range(1100)):
		if(NewDistanceTransformmatrix[i,j] != 0):
        	 values[0] =goalDistanceTransform[i,j];
        	 values[1] =goalDistanceTransform[i-1,j]+1;
        	 values[2] =goalDistanceTransform[i+1,j]+1;
        	 values[3] =goalDistanceTransform[i,j-1]+1;
        	 values[4] =goalDistanceTransform[i,j-1]+1;
        	 goalDistanceTransform[i,j] = min(values)#np.sqrt((i-911)*(i-911)+(i-1035)*(j-1036)) 

#for i in reversed(range(0,11)):
 #   print i 
path = np.zeros((1177,1102));
values = np.zeros(4);
print goalDistanceTransform[145,145]
a  = goalDistanceTransform.max();
b = goalDistanceTransform.min();
print a,b
#for i in range(1177):
 #   for j in range(1102):
  #      print i,j
   #     goalDistanceTransform[i,j] = (goalDistanceTransform[i,j]-b)*255/(a-b)+0

#for i in range(1,1176):
"""
	#for j in range(1,1101):
i = 145
j = 145		#if (i ==145 and j ==145):
path[i,j] = 255;
i_n=i ;
j_n=j;
#print "92,145"
#print goalDistanceTransform[92,145]
#print "93,145"
#print goalDistanceTransform[93,145]
#print "92,145"
#print goalDistanceTransform[92,145]

while(i_n !=811 or j_n != 980):

    print i_n,j_n
  #  i_n_previous = i_n;
   # j_n_previous = j_n;
   # print goalDistanceTransform[i_n,j_n]
	#	    values[0] =goalDistanceTransform[i_n,j_n];
    values[0] =goalDistanceTransform[i_n-1,j_n]
    values[1] =goalDistanceTransform[i_n,j_n-1]
    values[2] =goalDistanceTransform[i_n+1,j_n]
    values[3] =goalDistanceTransform[i_n,j_n+1]

    a = np.argmin(values);
    if (a==0):
        i_n = i_n-1;
        j_n = j_n;
    if (a==1):
        i_n=i_n
        j_n= j_n-1;
    if (a==2):
        i_n=i_n+1
        j_n= j_n;
    if (a==3):
        i_n=i_n;
        j_n= j_n+1;
    path[i_n,j_n] = 255;
    #i_n_after = i_n;
    #j_n_after = j_n;
"""
cv2.imwrite('/home/pulkit/Desktop/pathfinal.jpg',path);










