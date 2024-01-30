from numpy import *
import math as mh
Nbp = [2]
A = 3
L = [2]
while A<=1000:
    A += 1
    B = 1
    E = 0
    while B <= mh.sqrt(A) and E != 1:
        C = A/B
        B += 1
        if C == round(C , 0):
            E = 1
        
    if E == 0:
        Nbp.append(A)

print(Nbp)