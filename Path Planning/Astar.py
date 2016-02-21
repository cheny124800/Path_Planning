import numpy as np 
import cv2 
from PIL import Image
import math 
#Code Does not seem to be working but it is added as a lots of work was done on it. As it was written please have a lool

def Heuristic(X,goal):
	#X = np.asarray(X,'object')
	#goal = np.asarray(goal,dtype='object');
	d = np.sqrt(sum((X-goal)*(X-goal)));
	return d
def Historic(a,b):
	a = np.asarray(a,dtype='object');
	b = np.asarray(b,dtype='object');
	c = np.sqrt(sum((a-b)*(a-b)));
	return c;
def feasiblepoint(point,map):
	point = np.asarray(point,dtype='uint32');
	[a,b] = np.shape(map);
	feasible = True ;
	if not [np.logical_and((point[0] >= 0 and point[0]<a),(point[1] >=0 and point[1]<b),(map[point]==0))]:
		feasible = False
	return feasible
def checkpath(n,newpos,map):

    feasible = True;
    n = np.asarray(n,dtype='object');
    newpos=np.asarray(newpos,dtype='object')
    dir = np.arctan((newpos[0]-n[0])/(newpos[1]-n[1]));
    a= math.ceil(np.sqrt(sum((n-newpos)*(n-newpos))));
    #print a 
    a=int(a);
    for  i in [float(j)/2 for j in range(0,2*a,1)]:
    	posCheck=np.asarray([],dtype='float64');
        posCheck=n+i*np.asarray([math.sin(dir), math.cos(dir)]);
        if not [np.logical_and((feasiblepoint([math.ceil(posCheck[0]),math.ceil(posCheck[1])],map)),
			(feasiblepoint([math.floor(posCheck[0]),math.floor(posCheck[1])],map)),)]:
        	if not [np.logical_and((feasiblepoint([math.floor(posCheck[0]),math.ceil(posCheck[1])],map)),
			(feasiblepoint([math.ceil(posCheck[0]),math.floor(posCheck[1])],map)),)]:

				feasible = False;
				break
        if not (feasiblepoint(posCheck,map)):
			feasible = False;
    return feasible

source = np.asarray([145,145],dtype='object');
goal = np.asarray([811,920],dtype='object');
display = True;
map = cv2.imread('/home/pulkit/Downloads/4_1_map.bmp');
map=cv2.cvtColor(map,cv2.COLOR_BGR2GRAY)
map = np.asarray(map);   
R,C = np.shape(map)
print R,C  
############################################3
#X = np.array([1,2,3]);
#goal= np.asarray([4,5,6]);
#H = Heuristic(X,goal);
#print H 
##########################################3
#cv2.imwrite('/home/pulkit/Desktop/4_1_map.bmp',map);
#map_new = np.zeros((1177,1102));
#map_new[1:1176,1:1101] = map;
#print source[0] # check point

if not feasiblepoint(source,map):
	print "code in not working "
if not feasiblepoint(goal,map):
	print "code is not working"
pathfound = False ;
counter = 0 ;
closed = np.ones(np.shape(map));
closedlist = np.asarray([[]]);
#Q=[source 0 heuristic(source,goal) 0+heuristic(source,goal) -1];
Q = np.asarray([[]]);
Q = np.asarray([[source[0],source[1],0 ,Heuristic(source,goal), 0+Heuristic(source,goal) ,-1]]);
#print np.shape(Q)
#print Q[0];
#check for arg min #print np.argmin(Q[5],axis=0);
while (np.shape(Q)[1]>0) :
	#print 1
	I = np.argmin(Q,axis=0);
	n=Q[I[5],:];
	#print n ;
	#if (I[5]==0):#dangerous path be sure to check out if the code is not running perfectly 
	#	Q=np.asarray([[]]);
	#else:
	Q = np.delete(Q,I[5],0);
	print Q.size
	if (Q.size == 0):
		Q = np.asarray([[]])

	#print Q;
	if (n[0]==goal[0] and n[1]==goal[1]):
		pathfound=True;
		break
	rx = np.asarray([1]);
	ry = np.asarray([1]);
	mx = np.asarray([0,2,1,1]);
	my = np.asarray([1,1,0,2]);
	#print np.shape(mx)[0];
	for i in range(0,np.shape(mx)[0]):
		#print i 
		#print i ;
		newPos = np.asarray([n[0]+mx[i]-rx[0],n[1]+my[i]-ry[0]],dtype='object');
		#print newPos
		if (checkpath([n[0],n[1]],newPos,map)):
			if (closed[newPos[0],newPos[1]] != 0):
				print newPos
				historicCost=n[2]+Historic(np.asarray([n[0],n[1]]),newPos);
				#print historicCost
				heuristicCost=Heuristic(newPos,goal);
				#print heuristicCost
				totalCost=historicCost+heuristicCost;
				#print totalCost
				add=True;
				#print ((Q[:,0]==newPos[0]).argmax() *(Q[:,1]==newPos[1]).argmax())
				if Q.size != 0:
					o,p = np.where(Q[:,0:2]==newPos)
					#print ((Q[:,0]==newPos[0]).argmax()==(Q[:,1]==newPos[1]).argmax())
                    #o,p = np.where(Q[:,0:2]==newPos);
					if (o==p).all():
						I = np.where(Q[:,0:2]==newPos);
						if (Q[I[0],4]<totalCost): 
							add=False;
						else:
							Q = np.delete(Q,I,0);
					        add=True ;

				if add == True :
					#print "size of Q",Q.size
					#print Q 
					if  (Q.size != 0 ):
						Q=np.vstack([Q,[newPos[0],newPos[1] ,historicCost ,heuristicCost ,totalCost ,np.shape(closedlist)[0]+1]]);
					if  (Q.size == 0) :

						Q = np.zeros((1,6));
						Q = np.asarray([[newPos[0],newPos[1] ,historicCost ,heuristicCost ,totalCost ,np.shape(closedlist)[0]+1]]);
	#print Q
	closed[n[0],n[1]] = 0;

	if closedlist.size == 0:
		closedlist = n;
	else :
		closedlist = np.vstack([closedlist,n]);
	
   

pathmap = np.zeros((1177,1102));
path = np.asarray([n[0:2]]);
prev=n[5];
while prev > 0 :
	path = np.vstack([closedlist[0:2],path])
	prev = closedlist[prev,5];
for i in range(np.shape(path)[0]):
	pathmap[path[i,0],path[i,1]] = 255;
cv2.imwrite('/home/pulkit/Downloads/4_1_map.bmp',pathmap)



			#print "code"
            #print "code"
	
	#break
	#break
#print Q;	


#print Q[3]
