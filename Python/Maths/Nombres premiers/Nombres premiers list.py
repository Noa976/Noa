from sympy import *
A=1
Nbp=[]
fin=100
while A<=fin-1:
    A+=1
    if isprime(A)==true:
        Nbp.append(A)
print(f'Les {len(Nbp)} premiers nombres premiers de 1 à {fin} sont:{Nbp}')

















