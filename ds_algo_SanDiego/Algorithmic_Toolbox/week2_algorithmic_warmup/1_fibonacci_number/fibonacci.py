# Uses python3
import sys

def calc_fib(n):
    
    fib_prev = 0
    fib_cur = 1
    if (n==0):
        return fib_prev
    if (n==1):
        return fib_cur
    
    for i in range(1,n):
        fib_cur, fib_prev = fib_cur + fib_prev, fib_cur

    return fib_cur

input = sys.stdin.read()
print(calc_fib(input))
