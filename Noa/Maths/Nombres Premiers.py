import numpy as np
import math as mh
Nbp = []
A = 1
L = [2]
while A<=100:
    A += 1
    B = 0
    E = 0
    while L[B] <= mh.sqrt(A) and E != 1:
        C = A/L[B]
        B += 1
        if C == round(C , 0):
            E = 1
        
    if E == 0:
        Nbp.append(A)

print(Nbp)