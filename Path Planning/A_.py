import numpy as np 
import cv2 
from PIL import Image
import math 
# Path that we have is not a having a 10 pixels accuracy but it can be created given a distance transform 
#and converting it into a map having distance less than 10 pixels as an obstacles and then moving on the path 
#here in this case initial point is (144,144) and thne final point is (811,920) as the point given in the question 
#is an obstacle we have a solution 
map = Image.open('4_2_distance_transform.png',);
map= np.asarray(map);   
R,C = np.shape(map[:,:,0]);
print R,C
map_new = np.zeros((R+1,C+1));
map_check =255* np.ones((R+1,C+1));
map1= np.zeros((R,C));
number = 0
#From the Distance Transform map in the question convert it into another map where map[i,j] < 10 => Obstacle  or else it is a possible path
for i in range(R):
	for j in range(C):
		print i,j
		if (map[i,j,0] <= 10):
			map1[i,j] = 255;
		else :
			map1[i,j] = 0;
			number = number + 1 ;
cv2.imwrite('4_2_distance_transformdash.png',map1)
map_new[1:R+1,1:C+1] = map1 # map which will have the path of the body 
map_check[1:R+1,1:C+1] = map1 # map to check whether a point is an obstacle or not 
Node  = np.ones((R+1,C+1));    # Node set which tells whether the point has been visited or not 
Node[1:R+1,1:C+1] = map1
prev = np.zeros((R,C));      # Not really important it doesn't serve the purpose 
Source = np.asarray([145,145]);
Goal = np.asarray([811,920]);
path = np.zeros((R,C));
print Node[145,145]
print map1[145,145];
number = 1124909;
current = Source ;
counter = 100 ;
# Classical implementation of A Star given below 
while (number != 0) :
	number = number -1 
	mi = np.asarray([1,1,1,0,-1,-1,-1,0]);
	mj = np.asarray([-1,0,1,1,1,0,-1,-1]);
	values = 5000*np.ones(8);
	for i in range(np.shape(mi)[0]):
		n_new = np.asarray([current[0]+mi[i],current[1]+mj[i]]);
		print n_new
		a = Node[n_new[0],n_new[1]];
		if (a == 0):
			values[i] = np.sqrt(sum((n_new-Goal)*(n_new-Goal)))+np.sqrt(sum((n_new-Source)*(n_new-Source)));
	map_check[current[0],current[1]]=255;	
	for j in values.argsort():
		if (map_check[current[0]+mi[j],current[1]+mj[j]]!=255):
			break
	prev[current[0]+mi[j],current[1]+mj[j]]=255;
	current = np.asarray([current[0]+mi[j],current[1]+mj[j]])
	map_new[current[0],current[1]]=255;
	Node[current[0],current[1]] = 1

	if (current[0]==Goal[0]) and (current[1]==Goal[1]):
		break
print number 
cv2.imwrite('/home/pulkit/Desktop/aaa.png',map_new)



