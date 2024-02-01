import math as mh
T= input("Equation du eme degré: ")
print(type(T)) #    ffichz le type de T
T = int(T) #transforme en entier
if T == 1:
    nom= input("nom de l'inconnue : ")
    A = float(input('inconnue gauche : '))
    if A == round(A):
     A = round(A)
    C = float(input('inconnue droite : '))
    if C == round(C):
     C = round(C)
    B = float(input('Opération de gauche : '))
    if B == round(B):
     B = round(B)
    D = float(input('Opération de droite : '))
    if D == round(D):
     D = round(D)
    print('Equation du 1er degré:')
    print(f'{A}{nom} + {B} = {C}{nom} + {D}')
    if A-C==0:
       print(f'Vrai pour tout {nom}')
    else:
     Réponse = (D-B)/(A-C)
     if Réponse== round(Réponse):
      Réponse = round(Réponse)
      print(f'{nom} = {Réponse}')
    

if T == 2:
    a = float(input('a de x²'))
    b = float(input('b de x'))
    c = float(input('c'))
    delta = b**2-4*a*c
    if delta > 0:
        x1 = (-b + mh.sqrt(delta))/(2*a)
        x2 = (-b - mh.sqrt(delta))/(2*a)
        if not round(x1,9)==x1:
            if x1**2==round(x1**2):
                print(f'x1 = {x1**2} ~ {x1}')
            else:
                print(f'x1~ {x1}')
        else:
            print(f'x1 = {x1}')


        if not round(x2,9)==x2:
            if x2**2==round(x2**2):
                print(f'x2 = {x2**2} ~ {x2}')
            else:
                print(f'x2 ~ {x2}')
        else:
            print(f'x2 = {x2}')

    if delta == 0:
        x = -b / (2*a)
        if not round(x,9)==x:
            if x**2==round(x**2):
                print(f'x = {x**2} ~ {x}')
            else:
                print(f'x ~ {x}')
        else:
            print(f'x = {x}')

    if delta < 0:
        print("La valeur de x ne peut pas être définie ")
