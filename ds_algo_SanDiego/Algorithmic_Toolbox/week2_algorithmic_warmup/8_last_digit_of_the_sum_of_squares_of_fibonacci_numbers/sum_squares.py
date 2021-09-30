from sys import stdin

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


def fibonacci_sum_squares_fast(n):
    period_len, elements = get_period(10)
    return (elements[n % period_len] * (elements[n % period_len] + elements[n % period_len - 1]))%10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_fast(n))

