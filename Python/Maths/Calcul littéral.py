from sympy import *
def DevD():
    Inconnues=input('Inconnues : ')
    inconnue1=input('nom de l''inconnue : ')
    A=float(input('A = '))
    B=float(input('B = '))
    C=float(input('C = '))
    D=float(input('D = '))
    A1=A*C
    A2=A*D
    A3=B*C
    A4=B*D
    if round(A1)==A1:
        A1=round(A1)
    if round(A2)==A2:
        A2=round(A2)
    if round(A3)==A3:
        A3=round(A3)
    if round(A4)==A4:
        A4=round(A4)
    
    if ('A' in Inconnues and 'C' in Inconnues) or ('a' in Inconnues and 'c' in Inconnues):
        A32=A2+A3
        if A32==0:
            if A4 <0:
                print(f'{A1}{inconnue1}² - {-A4}')
            else:
                print(f'{A1}{inconnue1}² + {A4}')
        else:
            if A4<0 and not A32<0:
                print(f'{A1}{inconnue1}² + {A32}{inconnue1} - {-A4}')
            elif A32<0 and not A4<0:
                print(f'{A1}{inconnue1}² - {-A32}{inconnue1} + {A4}')
            elif A32<0 and A4<0:
                print(f'{A1}{inconnue1}² - {-A32}{inconnue1} - {-A4}')
            else:
                print(f'{A1}{inconnue1}² + {A32}{inconnue1} + {A4}')

    if ('A' in Inconnues and 'D' in Inconnues) or ('a' in Inconnues and 'd' in Inconnues):
        A32=A1+A4
        if A32==0:
            if A3<0:
                print(f'{A2}{inconnue1}² - {-A3}')
            else:
                print(f'{A2}{inconnue1}² + {A3}')
        else:
            if A32<0 and not A3<0:
                print(f'{A2}{inconnue1}² - {-A32}{inconnue1} + {A3}')
            elif A3<0 and not A32<0:
                print(f'{A2}{inconnue1}² + {A32}{inconnue1} - {-A3}')
            elif A32<0 and A3<0:
                print(f'{A2}{inconnue1}² - {-A32}{inconnue1} - {-A3}')
            else:
                print(f'{A2}{inconnue1}² + {A32}{inconnue1} + {A3}')
            
    if ('B' in Inconnues and 'C' in Inconnues) or ('b' in Inconnues and 'c' in Inconnues):
        A32=A1+A4
        if A32==0:
            if A2<0:
                print(f'{A3}{inconnue1}² - {-A2}')
            else:
                print(f'{A3}{inconnue1}² + {A2}')
        else:
            print(A2)
            if A32<<0 and not A2<0:
                print(f'{A3}{inconnue1}² - {-A3}{inconnue1} + {A2}')
            elif A2<<0 and not A32<0:
                print(f'{A3}{inconnue1}² + {A32}{inconnue1} - {-A2}')
            elif A32<0 and A2<0:
                
                print(f'{A3}{inconnue1}² - {-A32}{inconnue1} - {-A2}')
            else:
                print(f'{A3}{inconnue1}² + {A32}{inconnue1} + {A2}')
    if ('B' in Inconnues and 'D' in Inconnues) or ('b' in Inconnues and 'd' in Inconnues):
        A32=A2+A3
        if A32==0:
            if A1<0:
                print(f'{A4}{inconnue1}² - {-A1}')
            else:
                print(f'{A4}{inconnue1}² + {A1}')
        else:
            if A32 < 0 and not A1 < 0:
                print(f'{A4}{inconnue1}² - {-A32}{inconnue1} + {A1}')
            elif A1 < 0 and not A32 < 0:
                print(f'{A4}{inconnue1}² + {A32}{inconnue1} - {-A1}')
            elif A32 < 0 and A1 < 0:
                print(f'{A4}{inconnue1}² - {-A32}{inconnue1} - {-A1}')
            else:
                print(f'{A4}{inconnue1}² + {A32}{inconnue1} + {A1}')




def factoriser_expression():
    # Saisie de l'expression littérale
    expression_str = input("Entrez l'expression littérale : ")

    # Ajoutez une note à l'utilisateur pour explicitement spécifier les coefficients des variables
    print("Note : Entrez les coefficients explicitement. Par exemple, utilisez '3*a' au lieu de '-3a'.")

    # Définition des symboles
    x, a, b = symbols('x a b')

    try:
        # Conversion de la chaîne en expression SymPy
        expression = sympify(expression_str)

        # Factorisation de l'expression
        factored_expression = factor(expression)

        print("Expression factorisée :", factored_expression)

    except Exception as e:
        print("Erreur :", e)

DevD()

