# Uses python3
import sys
import itertools

def subsetSum(S, n, a, b, c, lookup):

    if a == 0 and b == 0 and c == 0:
        return True
    if n < 0:
        return False

    key = (a,b,c,n)

    if key not in lookup:

        A = False
        if a - S[n] >= 0:
            A = subsetSum(S, n - 1, a - S[n], b, c, lookup)
        
        B = False
        if not A and (b - S[n] >= 0):
            B = subsetSum(S, n- 1, a, b - S[n], c, lookup)
        
        C = False

        if (not A and not B) and (c - S[n] >= 0):
            C = subsetSum(S, n-1, a, b, c - S[n], lookup)

        lookup[key] = A or B or C

    return lookup[key]

        



def partition3(S):

    if len(S) < 3:
        return 0
    
    lookup = {}

    total = sum(S)

    if (total % 3) == 0 and subsetSum(S, len(S) - 1, total/3, total/3, total/3, lookup):
        return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

