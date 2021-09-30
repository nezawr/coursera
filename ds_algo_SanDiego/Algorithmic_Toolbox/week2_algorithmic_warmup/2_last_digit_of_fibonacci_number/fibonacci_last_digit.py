# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for i in range(1,n):
        previous, current = current, (previous + current) %10

    return current % 10

if __name__ == '__main__':
    input = input()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
