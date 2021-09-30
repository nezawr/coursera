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

a = []
b = [1]
c = [1,2,3]
d = [2,3,1]
e = [3,7,5,5,5,2]
randomized_quick_sort(a,0,0)
randomized_quick_sort(b,0,0)
#assert randomized_quick_sort(c,0,2) == [1,2,3]
randomized_quick_sort(d, 0, 2) == [1,2,3]
randomized_quick_sort(e,0, 5) == [2,3,5,5,5,7]
assert e == [2,3,5,5,5,7]
assert b == [1]
assert d == [1,2,3]
assert a == []
