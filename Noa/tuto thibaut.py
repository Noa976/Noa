'''import numpy as np
A = np.array([2,5,4,1]) #definition d'un tableau 1D
B = np.array([[2,0,1,2],
              [1,0,2,4]]) # definition d'un tableau 2D
b = B[1,3]
print('b', b)
N = 10
S = 0
for i in range(N):
    S = S + i
'''
T = 0
i = 0
g = 0
while T <= 30:
    T += i
    i += 1
    print('T', T)
    if T >= 20 and g == 0:
        print('on a dépassé la première barrière de 20')
        g += 1
"""
age_noa = input('Donne moi ton age Noa')
print("l'age de Noa est", age_noa)
print(f"Noa a {age_noa} ans")
"""
f = open("cccava.txt") # lire un fichier
lines = f.readlines() #recupérer les lignes d'un fichier
print('l', lines)

#import numpy as np

# donne un nombre aléatoire entre 0 et 1
'''x = 1+2*np.random.random((2,3))
print('x', x)

if x[0,1] >= 2:
    print("Les poules vont pondre des oeufs ce soir")
elif x[0,1] >= 1.5:
    print("Les poules ne pondront pas ce soir")
else:
    print("Les poules vont se faire manger par le renard")
'''

V = [1, 2,0,8]
print('tailel v', len(V))

x = 13
print('reste', x%3)
print('quotient', x//3)

# definition d'une fonction
def patate_douce(x, m=2):
    v = 3
    for i in [2,4]:
        v += i*x  # v = v + i*x
    return v

'''import numpy as np  # traiter les tableaux
import matplotlib.pyplot as plt   # tracer des graphes

X = np.arange(0, 8*np.pi, 10**-4)   # l'axe des abysses qui va de 0 à 8pi # arange(debut, fin, pas)
Y = np.sin(X)   # le sinus de l'axe des abysses

plt.plot(X, Y) # tracer
plt.show() # afficher

print("c", patate_douce(3))'''