from itertools import permutations
import math

n = 5

print(math.factorial(n))

perm = list(permutations(range(1,n+1)))

for i in perm:
    print(' '.join(map(str,i)))