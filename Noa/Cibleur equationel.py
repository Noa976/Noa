import math as mh
x = -10
Eqeme = float(input('Equation du eme degré'))
if Eqeme == 4:
    e = float(input('e de x4 '))
else:
    e=0

if Eqeme >= 3:
    d = float(input('d de x3 '))
else:
    d=0
if Eqeme >= 2:
    c = float(input('c de x2 '))
else:
    c=0

if Eqeme >= 1:                                  #pas content =<
    b = float(input('b de x '))
else:
    b=0

a = float(input('a '))
result = float(input('result '))
L = list()
while x <= 10:
   x = x+10**-5
   y = a + x*b + x**2*c + x**3*d + x**4*e
   if round(y, 4) == result and not round(x, 3) in L :
        print('x',round(x, 3))
        L.append(round(x,3))


   
