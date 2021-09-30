#Uses python3

import sys

sys.setrecursionlimit(200000)

def build_reverse_graph(adj):
    reverse_adj = [[] for i in range(len(adj))]
    for v, neighbours in enumerate(adj):
        for w in neighbours:
            reverse_adj[w].append(v)
    return reverse_adj

def explore_with_order(vertex, adj, visited, order):
    visited[vertex] = True
    for w in adj[vertex]:
        if not visited[w]:
            explore_with_order(w, adj, visited, order) 
    order.append(vertex)

def explore(vertex, adj, visited):
    visited[vertex] = True
    for w in adj[vertex]:
        if not visited[w]:
            explore(w, adj, visited) 

def dfs(adj):
    visited = [False for i in range(len(adj))]
    order = []
    for vertex in range(len(adj)):
        if not visited[vertex]:
            explore_with_order(vertex, adj, visited, order)
    return order

def number_of_strongly_connected_components(adj):
    result = 0
    #write your code here
    visited = [False for i in range(len(adj))]
    reverse_adj = build_reverse_graph(adj)
    post_order = dfs(reverse_adj)
    for vertex in reversed(post_order):
        if not visited[vertex]:
            result += 1
            explore(vertex, adj, visited)
    return result





if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
