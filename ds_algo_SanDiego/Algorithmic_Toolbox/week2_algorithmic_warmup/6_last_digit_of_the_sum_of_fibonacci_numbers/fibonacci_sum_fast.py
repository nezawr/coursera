import sys
import random

def get_period(n):
    length, fib_cur, fib_prev  = 1, 1, 0
    period = [0,1]
    if (n<=1):
        return (n,[1])
    while (True):
        fib_cur, fib_prev = (fib_cur + fib_prev) % n, fib_cur
        period.append(fib_cur)
        if (fib_cur == 1 and fib_prev == 0):
            
            break
        length += 1    
    return (length, period[:-2])

def fibonacci_sum_naive(n):
    fib_prev = 0
    fib_cur = 1
    sum = 1
    if (n<=1):
        return n 
    
    for i in range(1,n):
        fib_cur, fib_prev = fib_cur + fib_prev, fib_cur
        sum += fib_cur

    return sum % 10

def fibonacci_sum_fast(n):
    n += 1
    period_len, elements = get_period(10)
    multiples = n // period_len
    remainder = n % period_len
    Sum = 0
    Sum += ((sum(elements) % 10) * multiples) % 10
    Sum += sum(elements[:remainder]) % 10
    return Sum % 10
    

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input.split()[0])
