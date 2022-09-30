"""
Luis Pacheco / Neobrutal
in rv s d=0.1 n=2
in ru s d=0.1 n=2
in su s d=0.0 n=2
in nu s d=2.0 n=2
in sv s d=0.0 n=2
in nv s d=1.0 n=2
in r s d=1.0 n=2
out vertices v
out edges s
out polyline v
out polyedges s
"""

import math

startV = math.pi * sv  #cut v at start
stopV = math.pi * nv  #cut v at end
stepSizeV = rv #redundat but helps code redability
stepsV = int(abs(stopV-startV)//stepSizeV) #total v steps
startSkipV=int(abs(startV)/stepSizeV) #steps that get cut from start v
endSkipV=int(abs(stopV)/stepSizeV)#steps that get cut from end v


startU =  math.pi * su      #cut u at start
stopU = math.pi * nu  #cut u at end
stepSizeU = ru #redundat but helps code redability
stepsU = int(abs(stopU-startU)/stepSizeU)#total u steps
startSkipU=int(abs(startU)/stepSizeU) #steps that get cut from start u
endSkipU=int(abs(stopU)/stepSizeU) #steps that get cut from end v

baseLoops= r/stepSizeV


for stepV in range(startSkipV,endSkipV+1): #counts the V steps between the start and end cut parameters and starts iterating for each one
    print("stepV " + str(stepV)) #prints the current iteration of V
    v = stepV*stepSizeV #multiplies the current iteration times the step size on V
    print("v "+ str(v)) #optinal for debugging
    pointList = [] #creates a temporal point list for current V iteration
    edgeList =[]  #creates a temporal edge list for current V iteration
    for stepU in range(startSkipU,endSkipU+1):  #counts the U steps between the start and end cut parameters and starts iterating for each one
        u=stepU*stepSizeU #multiplies the current iteration times the step size on U
        
        x=math.sin(math.sin(v) * (math.cos(u) +math.sin(7*u)/7))
        y= math.sin(math.sin(v) * (math.sin(u) + math.cos(7*u)/7))
        if stepV == startSkipV:
            z= v + (stepSizeV/2)
        else:
            z= v + ((u*stepSizeV)/6.2831)
        
        p = [x,y,z]#creates a point
        pointList.append(p)#appends the point to our current V iteration list
        polyline.append(p) #appends the point to the polyline
    vertices.append(pointList) #appends our current V iteration list to our multidimensional vertices list
     
    for i in range(len(pointList)+1): #this  creates our edges list for our multidimensional vertices list
        v1 = i 
        v2 = i + 1
        ed = [v1,v2]
        edgeList.append(ed)
    for i in range(len(polyline)+1):#this  creates our edges list for our polyline vertices list
        v1 = i 
        v2 = i + 1
        ed = [v1,v2]
        polyedges.append(ed) 
    edges.append(edgeList)
        
polyline=[polyline]
#print(vertex) #optional for debugging
#print(stepsU) #optional for debugging
#print(stepsV)#optional for debugging
print("done") #prints done to the console to notify that everything worked as expecteds done to the console to notify that everything worked as expected