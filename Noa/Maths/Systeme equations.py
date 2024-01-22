Inconnues=float(input('Inconnues 2 ~ 4 = '))
if Inconnues==2:
    A = float(input('A de x = '))
    B = float(input('B de y = '))
    C = float(input('C = '))
    D = float(input('D = '))
    E= float(input('E = '))
    Y = (D-A*E+C)/(B-A)
    X = E-Y
    if X==round(X):
        X=round(X)
    if Y==round(Y):
        Y=round(Y)
    print(f'X = {X}')
    print(f'Y = {Y}')

if Inconnues==3:
    A = 0