from turtle import *
nbr=int(input('nombre de cercles'))
rayon=int(input('rayon des cercles'))
reset()
speed('fastest')
for i in range(0,500):
    rayon += 1
    circle(rayon)
    left(360/nbr)


done()