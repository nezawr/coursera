import sys 

def get_period(n):
    length = 1
    fib_prev = 0
    fib_cur = 1
    if (n<=1):
        return n
    while (True):
        fib_cur, fib_prev = (fib_cur + fib_prev) % n, fib_cur
        if (fib_cur == 1 and fib_prev == 0):
            break
        length += 1    
    return length


def fast_gcd(a,b):
    c = max(a,b)
    d = min(a,b)

    while (d):
        c, d = d, c%d
    return c


def get_fibonacci_last_digit(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for i in range(1,n):
        previous, current = current, (previous + current) % m

    return current 

        

def get_fibonacci_huge_fast(n, m):
    
    period_length = get_period(m)
    fibonnaci_num = n % period_length
    return get_fibonacci_last_digit(fibonnaci_num, m)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_fast(n, m))





