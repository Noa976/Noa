import numpy as np
import math as mh
import matplotlib
import matplotlib.pyplot as plt

A = 0
LA =10
LX=[]
LY=[]
plt.plot(LX,LY)
for i in range(LA):
    LY.append(mh.sin(A))
    A+=1
    LX.append(A/10)

plt.show