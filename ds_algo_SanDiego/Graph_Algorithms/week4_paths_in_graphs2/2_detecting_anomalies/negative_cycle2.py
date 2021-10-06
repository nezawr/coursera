#Uses python3

import sys
import math
import queue

def negative_cycle(adj, cost):

    #Add a dummy vertex connected to all other vertices with zero weighted edges
    dist = [float('inf') for i in range(len(adj) + 1)]
    dist[-1] = 0
    aug_adj = adj + [[i for i in range(len(adj))]]
    aug_cost = cost + [[0 for i in range(len(adj))]]
    #repeat |V| times, last iteration we might find cycles
    
    for i in range(len(aug_adj) + 1):
        #v and u are vertices
        for v in range(len(aug_adj)):
            for u_i, u in enumerate(aug_adj[v]):
                if dist[u] > dist[v] + aug_cost[v][u_i]:
                    dist[u] = dist[v] + aug_cost[v][u_i]
                    #relaxation on last iteration means vertex is on negative cycle
                    if i == len(aug_adj):
                        return 1
    return 0


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
    print(negative_cycle(adj, cost))
