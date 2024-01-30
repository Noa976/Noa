from turtle import *
from math import *

def A():
  left(60)
def B():
  left(240)
def ABdraw(x):
  if x==1:
    A()
  else:
    B()

ABlist1=[1,2,1,2,1,2,1,2,1,2,1,2]

ABlist2=[]

for z in ABlist1:
  if z==1:
    ABlist2.append(1)
    ABlist2.append(2)
    ABlist2.append(1)
    ABlist2.append(1)

  else:
    ABlist2.append(1)
    ABlist2.append(2)
    ABlist2.append(1)
    ABlist2.append(2)
ABlist3=[]
for z in ABlist2:
  if z==1:
    ABlist3.append(1)
    ABlist3.append(2)
    ABlist3.append(1)
    ABlist3.append(1)

  else:
    ABlist3.append(1)
    ABlist3.append(2)
    ABlist3.append(1)
    ABlist3.append(2)
ABlist4=[]
for z in ABlist3:
  if z==1:
    ABlist4.append(1)
    ABlist4.append(2)
    ABlist4.append(1)
    ABlist4.append(1)

  else:
    ABlist4.append(1)
    ABlist4.append(2)
    ABlist4.append(1)
    ABlist4.append(2)
    
ABlist5=[]
for z in ABlist4:
  if z==1:
    ABlist5.append(1)
    ABlist5.append(2)
    ABlist5.append(1)
    ABlist5.append(1)

  else:
    ABlist5.append(1)
    ABlist5.append(2)
    ABlist5.append(1)
    ABlist5.append(2)

ABlist6=[]
for z in ABlist5:
  if z==1:
    ABlist6.append(1)
    ABlist6.append(2)
    ABlist6.append(1)
    ABlist6.append(1)

  else:
    ABlist6.append(1)
    ABlist6.append(2)
    ABlist6.append(1)
    ABlist6.append(2)


print(f'Liste 1 : {ABlist1}')
print(f'Liste 2 :{ABlist2}')





def PairAB1(x):
  if x/2==round(x/2):
    A()
  else:
    B()


print(len(ABlist6))
print(len(ABlist5))
print(len(ABlist4))
print(len(ABlist3))
  
speed(0.5)
hideturtle()
up()
goto(-700,150)
down()

for l in ABlist1:
  ABdraw(l)
  forward(800/(len(ABlist1)))


up()

down()

for l in ABlist2:
  ABdraw(l)
  forward(800/(len(ABlist2)))


up()

down()

for l in ABlist3:
  ABdraw(l)
  forward(800/(len(ABlist3)))

up()

down()

for l in ABlist4:
  ABdraw(l)
  forward(800/(len(ABlist4)))


up()

down()

for l in ABlist5:
  ABdraw(l)
  forward(800/(len(ABlist5)))

up()

down()

for l in ABlist6:
  ABdraw(l)
  forward(800/(len(ABlist6)))


'''
reset()
hideturtle()
speed('fastest')
up()
goto(-400,150)
down()

for l in ABlist1:
  ABdraw(l)
  forward(50000/(len(ABlist1)))
  '''
















done()