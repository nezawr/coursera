def binary_search(a, x):
    left, right = 0, len(a)
    # write your code here
    while left < right:
        middle = (left + right)//2
        if a[middle] == x:
            return middle
        elif a[middle] < x:
            left = middle + 1
        else:
            right = middle - 1
    return -1


print(binary_search([1,2,3,4,5],10))
