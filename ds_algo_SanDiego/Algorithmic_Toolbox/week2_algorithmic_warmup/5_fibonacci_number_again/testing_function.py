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


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input.split()[0])
    print(get_period(n))