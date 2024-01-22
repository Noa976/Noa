from turtle import *
from math import *
reset()
speed('fastest')
t=0
a=radians(float(input('a')))
while t<=25000:
    t+=a
    goto(t*cos(t)/10,t*sin(t)/10)
done(
)