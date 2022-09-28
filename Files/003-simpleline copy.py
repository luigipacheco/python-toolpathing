"""
Luis Pacheco / Neobrutal Studio
in amount s d=3 n=2
in stepx s d=1 n=2
in stepy s d=0 n=2
in stepz s d=0 n=2
out verts v
out edges s
"""

for i in range(amount):
    x  = i * stepx
    y  = i *stepy
    z  = i *stepz
    vec = [x,y,z]
    verts.append(vec)
    
for i in range(amount-1):
    v1 = i
    v2 = i+1
    edges.append((v1,v2))


print(verts)
print(edges)