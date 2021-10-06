class Vertex:
    def __init__(self, id):
        self.id = id

def MakeSet(x):
    x.parent = x
    x.rank = 0

def Find(x):
    if x.parent == x:
        return x
    else:
        x.parent = Find(x.parent)
        return x.parent

def Union(x, y):
     xRoot = Find(x)
     yRoot = Find(y)
     if xRoot.rank > yRoot.rank:
         yRoot.parent = xRoot
     elif xRoot.rank < yRoot.rank:
         xRoot.parent = yRoot
     elif xRoot != yRoot: # Unless x and y are already in same set, merge them
         yRoot.parent = xRoot
         xRoot.rank = xRoot.rank + 1

v1, v2, v3, v4 = Vertex(1), Vertex(2), Vertex(3), Vertex(4)
MakeSet(v1), MakeSet(v2), MakeSet(v3), MakeSet(v4)
print(v1.parent)
print(v1.rank)
print(Find(v1))
Union(v1,v2), Union(v3,v4)
print(Find(v4))
Union(v1,v3)
print(Find(v1))
print(Find(v4))
