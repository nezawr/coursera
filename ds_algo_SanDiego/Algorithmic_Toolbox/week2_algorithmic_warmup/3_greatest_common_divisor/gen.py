import random 
import sys

#n = int(sys.argv[1])
myseed = int(sys.argv[1])
random.seed(myseed)

print(f'{random.randint(1,100000)} {random.randint(1,100000)}')
#print(n)
#print(' '.join([str(random.randint(1,1000)) for i in range(n)]))

