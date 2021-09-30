# Uses python3
import sys
import math

def get_optimal_operations(n):
    operations = ['add1','mul2','mul3']
    optimal_operations = [0] * (n+1)

    for i in range(2, n+1):
        optimal_operations[i] = float('inf')
        for op in operations:
            if op == 'add1':
                min_operations = optimal_operations[i - 1] + 1
                if min_operations < optimal_operations[i]:
                    optimal_operations[i] = min_operations
            elif op == 'mul2':
                if (i/2 == math.floor(i/2)):
                    min_operations = optimal_operations[int(i/2)] + 1
                    if min_operations < optimal_operations[i]:
                        optimal_operations[i] = min_operations
            if op == 'mul3':
                if (i/3 == math.floor(i/3)):
                    min_operations = optimal_operations[int(i/3)] + 1
                    if min_operations < optimal_operations[i]:
                        optimal_operations[i] = min_operations
    return optimal_operations


def optimal_sequence(n):
    sequence = []
    optimal_operations = get_optimal_operations(n)
    i = len(optimal_operations) - 1
    sequence.append(n)
    while i > 1:
        if (i%3 == 0):
            if (optimal_operations[i] == optimal_operations[int(i/3)] + 1):
                i = int(i/3)
                sequence.append(i)
                continue
        if (i%2 == 0):
            if (optimal_operations[i] == optimal_operations[int(i/2)] + 1):
                i = int(i/2)
                sequence.append(i)
                continue
        if (optimal_operations[i] == optimal_operations[i-1] + 1):
            i -= 1
            sequence.append(i)


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
