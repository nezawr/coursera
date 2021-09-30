# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    # write your code here
    n = len(values)
    sorted_tuples = sorted(zip(weights, values), key=lambda x:x[1]/x[0])
    weights, values = [list(tup) for tup in zip(*sorted_tuples)]
    for i in range(n-1,-1,-1):
        if (capacity == 0):
            break
        a = min(weights[i], capacity)
        value += a*(values[i]/weights[i])
        weights[i], capacity = weights[i] - a, capacity - a
    return round(value, 4)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
