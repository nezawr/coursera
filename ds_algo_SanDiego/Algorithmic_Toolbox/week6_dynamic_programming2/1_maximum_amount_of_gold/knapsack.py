# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    n = len(w)
    values = [[0 for i in range(W+1)] for j in range(len(w)+1)]
    for i in range(1,len(w)+1):
        for j in range(1,W + 1):
            current = values[i-1][j]
            if w[i-1] <= j:
                current = max(values[i-1][j - w[i-1]] + w[i-1], current)
            values[i][j] = current
    return values[len(w)][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
