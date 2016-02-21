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
for i in range(R):
	for j in range(C):
		print i,j
		if (map[i,j,0] <= 10):
			map1[i,j] = 255;
		else :
			map1[i,j] = 0;
#map1[580:585,234:239]=255;
cv2.imwrite('/home/pulkit/Desktop/4_2_distance_transformdash.png',map1)
#map1[580:585,234:239]=255;
#cv2.imwrite('/home/pulkit/Desktop/4_2_distance_transformdash1.png',map1)

#im = Image.open('/home/pulkit/Desktop/AssignmentCode/4_2_distance_transformdash.png');
#map = np.asarray(im)

print np.shape(map1)
map_new[1:R+1,1:C+1] = map1
map_check[1:R+1,1:C+1] = map1
Node  = np.ones((R+1,C+1));
prev  = np.asarray([]);
#map1  = np.ones((R,C));
#Node =np.append(Node,1);
#print Node 
number = 0
Node[1:R+1,1:C+1] = map1
#map1 = map1
#for i in range(R):
#	for j in range(C):
#		print i,j
		
 
 #       if (map[i,j]==0) : 
			#Node[i,j]=0
#			number = number + 1;
	     #if (map_new[i,j]==0):
#map1= map1;	     
#print number
#print np.shape(Node);

#print np.shape(Node)
#print Node[0]
prev = np.zeros((R,C));
Source = np.asarray([145,145]);
Goal = np.asarray([811,920]);
path = np.zeros((R,C));
print Node[145,145]
print map1[145,145];
number = 1124909;#print map[Source[0],Source[1]]

current = Source ;
counter = 100 ;
while (number != 0) :
	#Node[current[0],current[1]] == 1;
	number = number -1 
	#print current
	#I = np.where(Node == current[0]*C+current[1]);
	#print I
	#if (np.shape(I)[1] == 0):
		#break
	#Node = np.delete(Node,I)
	
	mi = np.asarray([1,1,1,0,-1,-1,-1,0]);
	mj = np.asarray([-1,0,1,1,1,0,-1,-1]);
	values = 5000*np.ones(8);
	for i in range(np.shape(mi)[0]):

		#print i
		n_new = np.asarray([current[0]+mi[i],current[1]+mj[i]]);
		print n_new
		#index = np.where(Node == n_new[0]*C+n_new[1]);
		a = Node[n_new[0],n_new[1]];
		#print a
		if (a == 0):
			values[i] = np.sqrt(sum((n_new-Goal)*(n_new-Goal)));
			#print values[i]
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
	#counter = counter -1 ;
	#if counter ==0 :
	#	break
	#break
print number 
cv2.imwrite('/home/pulkit/Desktop/aaa.png',map_new)
    #j = np.argmin(values)
    #prev = np.append(prev,current);
    #current = np.asarray([current[0]+mi[j],current[1]+mj[j]]);
    #break



#	break 



