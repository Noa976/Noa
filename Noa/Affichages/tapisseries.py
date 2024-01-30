from math import *
from turtle import *
from numpy import *
from random import *
colors = ['yellow', 'cyan', 'red', 'light blue', 'pink', 'blue', 'purple', 'green', 'orange']
for h in range(100):
 reset()
 speed("fastest")
 down()
 y=250
 up()
 goto(-250,y)
 down()
 def a1():
    fillcolor(Col1)
    begin_fill()
    
    right(45)
    forward(sqrt(50**2+50**2))
    left(45)
    back(50)
    left(90)
    forward(50)
    right(90)
    end_fill()
    fillcolor(Col2)
    begin_fill()
    right(45)
    forward(sqrt(25**2+25**2))
    left(135)
    forward(25)
    right(90)
    back(25)
    end_fill()
    fillcolor(Col3)
    begin_fill()
    forward(25)
    right(90)
    forward(25)
    left(45)
    forward(sqrt(25**2+25**2))
    left(135)
    forward(50)
    right(90)
    back(50)
    
    end_fill()


 def a2():
    forward(50)
    right(90)
    a1()
    left(90)
    back(50)
 def a3():
    forward(50)
    right(90)
    forward(50)
    right(90)
    a1()
    left(90)
    back(50)
    left(90)
    back(50)
 def a4():
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    a1()
    left(90)
    back(50)
    left(90)
    back(50)
    left(90)
    back(50)
 A=['a1','a2','a3','a4']
 
 Value1=choice(A)
 Value2=choice(A)
 Value3=choice(A)
 Value4=choice(A)
 for i in range(4): 

    for i in range(4):
        Col1=choice(colors)
        Col2=choice(colors)
        while Col1==Col2:
                Col2=choice(colors)
        Col3=choice(colors)
        while Col1==Col3 or Col2==Col3:
                Col3=choice(colors)
        
        if 'a1' in Value1:
            a1()
        if 'a2' in Value1:
            a2()
        if 'a3' in Value1:
            a3()
        if 'a4' in Value1:
            a4()
        forward(50)
        if 'a1' in Value2:
            a1()
        if 'a2' in Value2:
            a2()
        if 'a3' in Value2:
            a3()
        if 'a4' in Value2:
            a4()
        right(90)
        forward(50)
        left(90)
        back(50)
        if 'a1' in Value3:
            a1()
        if 'a2' in Value3:
            a2()
        if 'a3' in Value3:
            a3()
        if 'a4' in Value3:
            a4()
        forward(50)
        if 'a1' in Value4:
            a1()
        if 'a2' in Value4:
            a2()
        if 'a3' in Value4:
            a3()
        if 'a4' in Value4:
            a4()
        left(90)
        forward(50)
        right(90)
        forward(50)
    y+=-100
    up()
    goto(-250,y)
    down()
    





done()






