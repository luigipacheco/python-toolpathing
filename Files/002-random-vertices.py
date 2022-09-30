"""
Luis Pacheco / Neobrutal Studio
in n s d=3 n=2
out verts v
"""
import random

verts = [] 


for i in range(n):
    x  = random.randint(-10, 10)
    y  = random.randint(-10, 10)
    z  = random.randint(-10, 10)
    vec = [(x,y,z)]
    verts.append(vec)

#print(verts)
