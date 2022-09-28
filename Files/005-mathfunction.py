"""
Luis Pacheco / Neobrutal Studio
in n s d=100 n=2
in step s d=0.1 n=2
in scalez s d=0.1 n=2
out verts v
out edges s
"""
import math

def spiral():
    for i in range(n):
        x = math.cos(i*step) * i
        y = math.sin(i*step) * i
        z= math.sin(math.sqrt(x**2+y**2))*scalez
        p = [x,y,z]
        verts.append(p)

    for i in range(n-1):
        v1 = i
        v2 = i+1
        edges.append((v1,v2))
        
spiral()