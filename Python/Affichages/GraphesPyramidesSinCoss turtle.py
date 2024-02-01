from turtle import *
from math import *
reset()
speed('fastest')
t=0
a=radians(360/15+0.1)
while t<=25000:
    t+=a
    goto(t*cos(t)/5,t*sin(t)/5)
done(
)