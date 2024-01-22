import math as mh
T = input("Equation du eme degré")
print(type(T)) #    ffichz le type de T
T = int(T) #transforme en entier
if T == 1:
    A = float(input('inconnue gauche'))
    C = float(input('inconnue droite'))
    B = float(input('Opération de gauche'))
    D = float(input('Opération de droite'))
    Réponse = (D-B)/(A-C)
    print('Réponse', Réponse)

if T == 2:
    a = input('a de x²')
    b = input('b de x')
    c = input('c')
    delta = b**2-4*a*C
    if delta > 0:
        x1 = (-b + mh.sqrt(delta))/(2*a)
        x2 = (-b + mh.sqrt(delta))/(2*a)
        print(f'x = {x1}')
        print(f'x = {x2}')

    if delta == 0:
        x = -b / (2*a)
        print(f'x = {x}')

    if delta < 0:
        print("La valeur de x ne peut pas être définie ")
