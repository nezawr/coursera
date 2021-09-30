#Uses python3

import sys

clock = 1
cyclic = 0

def previsit(vertex, previsited):
    global clock
    previsited[vertex] = clock
    clock += 1

def postvisit(vertex, postvisited):
    global clock
    postvisited[vertex] = clock
    clock += 1

def explore(vertex, adj, visited, previsited, postvisited):
    global cyclic
    visited[vertex] = True
    previsit(vertex, previsited)
    for w in adj[vertex]:
        if visited[w]:
            if not postvisited[w]:
                cyclic = 1
        if not visited[w]:
            explore(w, adj, visited, previsited, postvisited)
    postvisit(vertex, postvisited)


    

def acyclic(adj):
    global cyclic
    visited = [False for i in range(len(adj))]
    previsited = [0 for i in range(len(adj))]
    postvisited = [0 for i in range(len(adj))]

    for vertex in range(len(adj)):
        if not visited[vertex]:
            explore(vertex, adj, visited, previsited, postvisited)

    return cyclic

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
