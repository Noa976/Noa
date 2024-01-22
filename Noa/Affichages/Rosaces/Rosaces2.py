from turtle import *
from colorsys import *
reset()
setup(800,800)
speed(25)
tracer(10)
width(2)
bgcolor("black")
for j in range(25):
    for i in range(20):
        color(hsv_to_rgb(i/15,j/25,1))
        right(88)
        circle(200-j*4,90)
        left(88)
        circle(200-j*4,90)
        right(180)
        circle(50,24)
done()