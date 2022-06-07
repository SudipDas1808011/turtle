from turtle import *
import random
colors = ["cyan","black","red","green","yellow"]

up()
goto(-200,0)
down()
pensize(6)
for i in range(3):
    up()
    fd(120)
    down()
    color(colors[i])
    circle(50)
for i in range(2):
    color(colors[i+3])
    up()
    backward(110+i*10)
    right(90)
    down()
    circle(50)
    left(90)

    

    
    
