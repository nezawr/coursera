import sys

def get_period(n):
    length, fib_prev, fib_cur  = 1, 0, 1
    period = [1,1]
    if (n<=1):
        return n
    while (True):
        fib_cur, fib_prev = (fib_cur + fib_prev) % n, fib_cur
        period.append(fib_cur)
        if (fib_cur == 1 and fib_prev == 0):
            break
        length += 1    
    return (length, period)

if __name__ == '__main__':
    input = sys.stdin.read()
    input.split()
    #print(get_fibonacci_huge_fast(n, m))