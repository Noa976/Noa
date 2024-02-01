import math as mh
import numpy  as np
def Equation1(A , B , C , D):
    if (A-C)==(B-D):
        x='x'
    elif (A-C)==0 and not (A-C)==(B-D):
        x=0
        print(f'x = 0')
    else:
        x=(D-B)/(A-C)
        print(f'x = {x}')
    


def Equation2(a,b,c):
    delta = (b*b)-(4*a*c)
    if delta > 0:
        x1 = (-b + mh.sqrt(delta))/(2*a)
        x2 = (-b - mh.sqrt(delta))/(2*a)
        
        print(f'Premier résultat = {x1}')
        print(f'Second résultat = {x2}')

    if delta == 0:
        x = -b / (2*a)

    if delta < 0:
        print("La valeur de x ne peut pas être définie ")


    


