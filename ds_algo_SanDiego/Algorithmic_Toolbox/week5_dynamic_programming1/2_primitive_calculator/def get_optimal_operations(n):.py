def get_optimal_operations(n):
    operations = ['add1','mul2','mul3']
    optimal_operations = [0] * (n)

    for i in range(2, n):
        optimal_operations[i] = float('inf')
        for op in operations:
            if op == 'add1':
                min_operations = optimal_operations[i - 1] + 1
                if min_operations < optimal_operations[i]:
                    optimal_operations[i] = min_operations
            if op == 'mul2':
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