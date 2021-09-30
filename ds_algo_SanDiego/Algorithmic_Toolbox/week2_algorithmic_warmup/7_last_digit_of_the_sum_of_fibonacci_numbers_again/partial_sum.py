import sys

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

def fibonacci_partial_sum_fast(from_, to_):
    to_ += 1
    period_len, elements = get_period(10)
    multiples_to, remainder_to = to_ // period_len, to_% period_len
    multiples_from, remainder_from = from_ // period_len, from_ % period_len
    sum_to, sum_from = 0, 0
    sum_to += ((sum(elements) % 10) * multiples_to) % 10
    sum_to += sum(elements[:remainder_to]) % 10
    sum_from += ((sum(elements) % 10) * multiples_from) % 10
    sum_from += sum(elements[:remainder_from]) % 10
    return (sum_to - sum_from) % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_fast(from_, to))

