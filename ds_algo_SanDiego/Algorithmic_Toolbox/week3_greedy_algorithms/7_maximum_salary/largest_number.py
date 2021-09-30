#Uses python3

import sys

def isGreaterOrEqual(n, m):
    
    if ((int(n+m) - int(m+n)) >= 0):
        return True
    else:
        return False 

def largest_number(digits):
    #write your code here
    answer = ""
    while len(digits) > 0:
        max_digit = str(0)
        for digit in digits:
            if isGreaterOrEqual(digit, max_digit):
                max_digit = digit
        answer += max_digit
        digits.remove(max_digit)
    return answer

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    data = data[1:]
    print(largest_number(data))


    #a = data[0]
    #b = data[1]
    #print(isGreaterOrEqual(a,b))

    
