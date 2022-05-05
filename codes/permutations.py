a="shr"
from itertools import permutations
# from sympy.combinatorics.partitions import Partition
# from sympy.combinatorics.permutations import Permutation
p=permutations(a)
cnt=0
for i in p:
    cnt+=1
    print(i)
p=list(p)
print(p)
for i in range(cnt):
    p[i]=list(p[i])
    print(p[i])