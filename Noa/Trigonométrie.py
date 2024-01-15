import numpy as n
import math as mh
I = input("An,Ad,H,O:")
Anrac = 0
Adrac = 0
Hrac = 0
Orac = 0
if 'An' in I:
    An = mh.radians(float(input('Angle = ')))
else:
    An = 0  

if 'Ad' in I:
    Ad = float(input('Adjacent = '))
else:
    Ad = 0  
    
if 'H' in I:
    H = float(input('Hypoténuse = '))
else:
    H = 0      
    
if 'O' in I:
    O = float(input('Opposé = '))
else:
    O = 0 
LA = n.arange(0,2,1)
for A in LA:
    if O == 0:
        if An != 0 and Ad != 0:
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
H = round(H, 15)
O = round(O,15)
Ad = round(Ad,15)
An = round(An, 15)

if not round(H, 9) == H:
	if round(H**2) == round(H**2, 5):
		H = round(H**2)
		Hrac = 1
          
if not round(An, 9) == An:
	if round(An**2) == round(An**2, 5):
		An = round(An**2)
		Anrac = 1
          
if not round(Ad, 9) == Ad:
	if round(Ad**2) == round(Ad**2, 5):
		Ad = round(Ad**2)
		Adrac = 1
          
if not round(O, 9) == O:
	if round(O**2) == round(O**2, 5):
		O = round(O**2)
		Orac = 1
          
if An == 0 or O == 0 or Ad == 0 or H == 0:
     print('Les informations sont insuffisantes pour établir les longueurs')

if Hrac == 0:
    print(f'Hypoténuse = {H}')
else:
     print(f'Hypoténuse = racine de {H} ~ {mh.sqrt(H)}')

if Adrac == 0:
    print(f'Adjacent = {Ad}')
else:
     print(f'Adjacent = racine de {Ad} ~ {mh.sqrt(Ad)}')

if Anrac == 0:
    print(f'Angle = {An}°')
else:
     print(f'Angle = racine de {An}° ~ {mh.sqrt(An)}°')


if Orac == 0:
    print(f'Opposé = {O}')
else:
     print(f'Opposé = racine de {O} ~ {mh.sqrt(O)}')