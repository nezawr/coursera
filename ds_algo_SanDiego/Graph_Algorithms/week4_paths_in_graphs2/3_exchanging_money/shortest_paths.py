#Uses python3

import sys
import queue

def bfs(adj, shortest, visited, u):
    visited[u] = True
    q = queue.Queue(maxsize=0)
    q.put(u)
    while not q.empty():
        u = q.get()
        for w in adj[u]:
            if not visited[w]:
                shortest[w] = 0
                visited[w] = True
                q.put(w)

def shortet_paths(adj, cost, s, distance, reachable, shortest):
    
    cycle_vertices = queue.Queue(maxsize=0)
    distance[s], reachable[s], shortest[s] = 0, 1, 1
    
    #repeat |V| times, last iteration we might find cycles
    for i in range(len(adj) + 1):
        for v in range(len(adj)):
            for u_i, u in enumerate(adj[v]):
                if distance[u] > distance[v] + cost[v][u_i]:
                    distance[u] = distance[v] + cost[v][u_i]
                    reachable[u] = 1
                    #relaxation on last iteration means vertex is on negative cycle
                    if i == len(adj):
                        cycle_vertices.put(u)
                        shortest[u] = 0

        visited = [False for i in range(len(adj))]
        while not cycle_vertices.empty():
            u = cycle_vertices.get()
            if not visited[u]:
                bfs(adj, shortest, visited, u)   



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s = data[0]
    s -= 1
    distance = [float('inf')] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

