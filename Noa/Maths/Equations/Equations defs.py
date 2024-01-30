import math as mh
import numpy  as np
def Equation1(A , B , C , D):
    print((D-B)/(A-C))

def Equation2(a,b,c):
    delta = (b*b)-(4*a*c)
    if delta > 0:
        x1 = (-b + mh.sqrt(delta))/(2*a)
        x2 = (-b - mh.sqrt(delta))/(2*a)
        print(f'Premier résultat = {x1}')
        print(f'Second résultat = {x2}')

    if delta == 0:
        x = -b / (2*a)
        print(f'Résultat = {x}')

    if delta < 0:
        print("La valeur de x ne peut pas être définie ")


def f(x):
    return 2*x + np.sin(x)

def Equation(f):


    return #solution de f(x)=0


Equation(f)
    


