# Uses python3
import sys
import random

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def partition3(a, l, r):
    #write your code here
    j = partition2(a, l, r)
    a[l], a[j] = a[j], a[l]
    x = a[l]
    p = l
    for i in range(l + 1, j + 1):
        if a[i] < x:
            p += 1
            a[i], a[p] = a[p], a[i]
    a[l], a[p] = a[p], a[l]
    return (p,j)


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
