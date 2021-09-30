import random
import sys
import os

test = int(sys.argv[1])
n = int(sys.argv[2])

for i in range(test):
    print('Test#' + str(i))

    os.system('python3 gen.py ' + str(n) + ' ' + str(i) + ' > input.txt')

    os.system('python3 model.py < input.txt > model.txt')
    os.system('python3 main.py < input.txt > main.txt')

    with open('model.txt') as f: model = f.read()
    print('Model: ', model)
    
    with open('main.txt') as f: main = f.read()
    print('Main: ', main)
    
    if model != main:
        random.seed(i)
        print(n)
        print(' '.join([str(random.randint(1,10)) for i in range(n)]))
        break
