from turtle import *
import random
import math
import time


def A(h,v,dim):
    up()
    goto(h,v)
    down()
    pensize(3)
    title("gg")
    left(75)
    fd(100*dim)
    x,y=pos()
    right(75)
    fd(15*dim)
    right(75)
    fd(100*dim)
    up()
    goto(h+(x-h)/2,math.tan(75*math.pi/180)*(x-h)/2+v)
    down()
    left(75)
    fd(41*dim)
    hideturtle()


