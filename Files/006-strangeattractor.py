"""
Luis Pacheco / Neobrutal Studio
in n s d=1000 n=2
in dt s d=0.01 n=2
out verts v
out edges s
"""

def lorenz(n, verts,edges):
        
    a = 10.0
    b = 28.0
    c = 8.0 / 3.0

    x = 0.01
    y = 0.01
    z = 0.02
    
    for i in range(n):
        dx = dt * a * (y - x)
        dy = dt * (x * (b - z) - y)
        dz = dt * (x * y - c * z)
        x = x + dx
        y = y + dy
        z = z + dz
        verts.append([x,y,z])
        
    for i in range(n-1):
        v1 = i
        v2 = i+1
        edges.append((v1,v2))

lorenz(n, verts,edges)

verts=[verts] 
edges=[edges]
       
print(verts)