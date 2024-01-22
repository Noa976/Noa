from math import *
from defs import *
from turtle import *
from numpy import *
import random
for i in range(100):
 reset()
 speed("fastest")
 up()
 y=250
 goto(-250,y)
 def a1():
    fillcolor("pink")
    begin_fill()
    
    right(45)
    forward(sqrt(50**2+50**2))
    left(45)
    back(50)
    left(90)
    forward(50)
    right(90)
    end_fill()
    fillcolor("yellow")
    begin_fill()
    right(45)
    forward(sqrt(25**2+25**2))
    left(135)
    forward(25)
    right(90)
    back(25)
    end_fill()
    fillcolor("cyan")
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
 
 Value1=random.choice(A)
 Value2=random.choice(A)
 Value3=random.choice(A)
 Value4=random.choice(A)
 for i in range(4):    
    for i in range(4):
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
    





done()






