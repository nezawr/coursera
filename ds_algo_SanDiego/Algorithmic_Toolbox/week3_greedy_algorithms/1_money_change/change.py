# Uses python3
import sys

def get_change(m):
    coins = 0
    while (m - 10 >= 0):
        m -= 10
        coins += 1
    while (m-5 >= 0):
        m-=5
        coins += 1
    while (m-1 >= 0):
        m-=1
        coins += 1
    return coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
