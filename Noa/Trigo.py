import numpy as n
import math as mh
I = input("An,Ad,H,O:")
if 'An' in I:
    An = float(input('An'))
else:
    An = 0  

if 'Ad' in I:
    Ad = float(input('Ad'))
else:
    Ad = 0  
    
if 'H' in I:
    H = float(input('H'))
else:
    H = 0      
    
if 'O' in I:
    O = float(input('O'))
else:
    O = 0 
LA = n.arange(0,2,1)
for A in LA:
    if O == 0:
        if An!=0 and Ad!=0:
            O = Ad*mh.tan(An)
        if An != 0 and H != 0:
            O = mh.sin(An)*H

    if Ad == 0:
        if An != 0 and H != 0:
            Ad = mh.cos(An)* H
        if An != 0 and O != 0:
            Ad = O/mh.tan(An)
    
    if H == 0:
        if Ad != 0 and An != 0:
            H = Ad/mh.cos(An)
        if O != 0 and An != 0:
            H = O/mh.sin(An)
    
    if An == 0:
        if Ad != 0 and H != 0:
            An = mh.acos(Ad/H)
        if O != 0 and H != 0:
            An = mh.asin(O/H)
        if O != 0 and Ad != 0:
            An = mh.atan(O/Ad)
An = mh.degrees(An)
print(f'Hypoténuse = {H}')
print(f'Adjacent = {Ad}')
print(f'Angle = {An}')
print(f'Opposé = {O}')