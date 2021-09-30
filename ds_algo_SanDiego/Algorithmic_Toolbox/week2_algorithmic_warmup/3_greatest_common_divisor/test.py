import random
import sys
import os

test = int(sys.argv[1])
#n = int(sys.argv[2])

for i in range(test):
    print('Test#' + str(i))

    os.system('python3 gen.py '  + str(i) + ' > input.txt')

    os.system('python3 fast_gcd.py < input.txt > model.txt')
    os.system('python3 gcd.py < input.txt > main.txt')

    with open('model.txt') as f: model = f.read()
    print('Model: ', model)
    
    with open('main.txt') as f: main = f.read()
    print('Main: ', main)
    
    if model != main:

        #print(' '.join([str(random.randint(1,1000)) for i in range(n)]))
        break
