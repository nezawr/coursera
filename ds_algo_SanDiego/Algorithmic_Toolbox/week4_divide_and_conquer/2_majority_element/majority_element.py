# Uses python3
import sys

def merge(a,b):
    result = [0] * (len(a) + len(b))
    i, j, k = 0, 0, 0
    while (i < len(a)) and (j < len(b)):
        if a[i] < b[j]:
            result[k] = a[i]
            k += 1
            i += 1
        else:
            result[k] = b[j]
            k += 1
            j += 1

    while (i < len(a)):
        result[k] = a[i]
        k += 1
        i += 1
    
    while (j < len(b)):
        result[k] = b[j]
        k += 1
        j += 1

    return result

def check_majority(a):
    i, n = 0, 0

    if (len(a)%2 == 1):
        n = len(a)//2 + 1
    else:
        n = len(a)//2 

    while (i < n):
        if a[i] == a[i + len(a)//2]:
            return True
        i += 1
    return False

def get_majority_element(a):

    if len(a) > 1:
        m = (len(a))//2
        b, bbool = get_majority_element(a[:m])
        c, cbool = get_majority_element(a[m:])
        A = merge(b, c)
        majority_bool = check_majority(A)
        return (A, majority_bool)
    return (a, True)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    A, bool = get_majority_element(a)
    if bool:
        print(1)
    else:
        print(0)
