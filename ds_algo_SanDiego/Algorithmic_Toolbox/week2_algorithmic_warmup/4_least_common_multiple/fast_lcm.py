import sys

def fast_gcd(a,b):
    c = max(a,b)
    d = min(a,b)

    while (d):
        c, d = d, c%d
    return c


def fast_lcm(a, b):
    gcd = fast_gcd(a,b)
    return int((a*b)/gcd)


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(fast_lcm(a, b))