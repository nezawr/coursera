# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    return number_of_inversions

def merge(a,b):
    result = [0] * (len(a) + len(b))
    inversions = 0
    positioned_b_elements = 0
    i, j, k = 0, 0, 0
    while (i < len(a)) and (j < len(b)):
        if a[i] <= b[j]:
            result[k] = a[i]
            inversions += (positioned_b_elements)
            i += 1
        else:
            result[k] = b[j]
            positioned_b_elements += 1
            j += 1

        k += 1

    while (i < len(a)):
        result[k] = a[i]
        k += 1
        i += 1
        inversions += (positioned_b_elements) #supposed to be len(b) of them
    
    while (j < len(b)):
        result[k] = b[j]
        k += 1
        j += 1

    return (result, inversions)


def merge_sort(A):
    if len(A) > 1:
        m = len(A)//2
        B, inversionsB = merge_sort(A[:m])
        C, inversionsC = merge_sort(A[m:])
        D, inversionsD = merge(B,C)
        return (D, inversionsD + inversionsB + inversionsC)
    return (A, 0)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    res, inversions = merge_sort(a)
    print(inversions)
    
    
