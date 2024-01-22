import numpy as n
import matplotlib.pyplot as plt
import matplotlib.animation as plta
from matplotlib.collections import LineCollection

'''np.arange(debut, fin, pas) #l'ensemble des valaeurs qui vont de début jusqu'à fin avec un pas de pas

np.sin

np.cos

np.sin(np.array(3,5,4))'''

Pas = 0.025
Debut = 20
Prec = 100
Intervale = 50
cmap = 'hot'

LX = []
LY = []
LA = n.arange(Debut,180,Pas)
for A in LA:
    T = 1
    Fin = 0
    X = []
    Y = []
    while not Fin == 1:
        T += A
        theta = 2*n.pi*T/360
        X.append(T*n.cos(theta)/Prec)
        Y.append(T*n.sin(theta)/Prec)
        if T>=20000:
            Fin = 1
    
    LX.append(X)
    LY.append(Y)

    #plt.plot(X, Y)
    #plt.show()
plt.rcParams["figure.figsize"] = (10,10)
fig, ax = plt.subplots()


print('shp', len(LX[1]))

def update(frame):
    xdata = LX[frame]
    ydata = LY[frame]
    ax.clear()
    ax.set_xlim([-200,200])
    ax.set_ylim([-200,200])
    colors = n.arange(len(ydata))
    #ax.scatter(xdata, ydata, c=colors, cmap='hsv', edgecolors='k')
    lines = [[(xdata[i], ydata[i]), (xdata[i+1], ydata[i+1])] for i in range(len(xdata)-1)]
    line_collec = LineCollection(lines, cmap=cmap)
    line_collec.set_array(range(len(xdata)-1)[::-1])
    ax.add_collection(line_collec)
    plt.title(f'A = {round(LA[frame], 2)}°; Pas = {Pas}; cmap={cmap}, Amax = 180')



plta.FuncAnimation(fig, update, frames=range(len(LX)), interval=Intervale)
plt.show()