from numpy import *
from math import *
i=3
Nbp = []
A = 1
Nbp.append(2)
for f in range(10):
    k=2
    e=0
    j=0
    while e==0 or sqrt(i) <= k:
        k += 1
        if i%k==0:
            e = 1
        j+=1
        
    if e == 0:
        Nbp.append(i)
    i +=1

print(Nbp)