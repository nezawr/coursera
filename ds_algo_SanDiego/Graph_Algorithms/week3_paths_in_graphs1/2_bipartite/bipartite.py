#Uses python3

import sys
import queue

def bfs_bipartite(adj, color, vertex):
    q = queue.Queue(maxsize=0)
    q.put(vertex)
    color[vertex] = 1
    while not q.empty():
        u = q.get()
        for w in adj[u]:
            if color[w] == -1:
                color[w] = 1 - color[u]
                q.put(w)
            elif color[w] == color[u]:
                return False

    return True


def bipartite(adj):
    #write your code here
    color = [-1 for i in range(len(adj))]

    for vertex in range(len(adj)):
        if color[vertex] == -1:
            #returns True is bipartite False otherwise
            if not bfs_bipartite(adj, color, vertex):
                return 0
    return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
