"""
Luis Pacheco / Neobrutal Studio
in u s d=4 n=2
in v s d=4 n=2
out vertices v
out vertgroup v
out edges s
"""
import math
def surface():
    for iv in range(v):
        lineV = []
        for iu in range(u):
            x= iv
            y= iu
            z = math.sin(iu*.5)**5*math.sin(iv*.5)
            p=[x,y,z]
            lineV.append(p)
            vertgroup.append(p)
        vertices.append(lineV)
        print(lineV)
        lineE=[]
        for i in range(len(lineV)):
            e1=i
            e2= i+1
            lineE.append([e1,e2])
        edges.append(lineE)
surface()