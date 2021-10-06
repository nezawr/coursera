#Uses python3
import sys
import math
from itertools import starmap

class Vertex:
    def __init__(self, id):
        #id is a tuple of x,y coordinates  
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

def get_cost(coordinates, i, j):
    x = (coordinates[i].id[0] - coordinates[j].id[0])**2
    y = (coordinates[i].id[1] - coordinates[j].id[1])**2
    return math.sqrt(x + y)

def get_edges(coordinates):
    edges = []
    for i in range(len(coordinates)):
        for j in range(len(coordinates)):
            if i != j:
                cost = get_cost(coordinates,i, j)
                edges.append((i,j,cost))
    return sorted(edges, key= lambda x: x[2])

    
#edges is a sorted non-decresing list of (i1,i2,cost) tuples 
#i1 and i2 are indices in coordinates list of the two vertices connected via edge weighted with cost
def Kruskal(edges, coordinates):
    total_cost = 0
    for vertex in coordinates:
        MakeSet(vertex)
    x = set()
    for edge in edges:
        if Find(coordinates[edge[0]]) != Find(coordinates[edge[1]]):
            total_cost += edge[2]
            x.add(edge)
            Union(coordinates[edge[0]], coordinates[edge[1]])
    return total_cost

def construct_vertex(x,y):
    return Vertex((x,y))

def minimum_distance(x, y):
    result = 0
    #write your code here
    coordinates = list(map(construct_vertex, x, y))
    #edges are tuples: (i1,i2, cost)
    edges = get_edges(coordinates)
    result = Kruskal(edges, coordinates)
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
