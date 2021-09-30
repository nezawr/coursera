
def merge(a,b):
    result = [0] * (len(a) + len(b))
    i, j, k = 0, 0, 0
    while (i < len(a)) and (j < len(b)):
        if a[i] < b[j]:
            result[k] = a[i]
            i += 1
        else:
            result[k] = b[j]
            j += 1

        k += 1

    while (i < len(a)):
        result[k] = a[i]
        k += 1
        i += 1
    
    while (j < len(b)):
        result[k] = b[j]
        k += 1
        j += 1

    return result

def merge_sort(A):
    if len(A) > 1:
        m = len(A)//2
        B = merge_sort(A[:m])
        C = merge_sort(A[m:])
        D = merge(B,C)
        return D
    return A 

assert(merge_sort([])) == []
assert merge_sort([1]) == [1]
assert merge_sort([2,3,1]) == [1,2,3]
print(merge_sort([2,3,2,7,6,1,6,6]))
print(merge_sort([54,26,93,17,77,31,44,55,20]))