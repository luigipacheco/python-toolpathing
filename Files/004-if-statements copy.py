"""
Luis Pacheco / Neobrutal Studio
in n s d=3 n=2
in step s d=1 n=2
out verts v
out edges s
"""

for i in range(n):
    x  = i*step
    y  = 0
    if i%2:
        z  = 0
    else:
        z = 1
    p = [x,y,z]
    verts.append(p)
    
for i in range(n-1):
    v1 = i
    v2 = i+1
    edges.append((v1,v2))

print(edges)
