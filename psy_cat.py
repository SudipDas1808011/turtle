from turtle import *
import random
import math

pensize(3)
title("Pussy_cat")
c=0
d=0

def parabola(x,size):
    y = math.sqrt(4*size*x)
    return -y
def upp_dwn(x,y):
    up()
    goto(x,y)
    down()
    
def drawing(x,size,span,k):
    global c,d
    upp_dwn(x,0)
    for i in range(span):
        color(random.choice(["red","blue","green","purple"]))
        y=parabola(i,size/2)
        if(c !=0):
            y*=-1
        if(k ==0):
            xx=x+i
        else:
            xx=x-i
        goto(xx,y)    
    if(c==0):
            c+=1
            end_fill()
            drawing(x,size,span,k)
            
            
    if(c==1 and d==0):
        c=0
        d+=1
        drawing(size-x,size,span,1)
    c=0
    d=0      
drawing(0,200,102,0)
drawing(20,200,82,0)
drawing(40,200,62,0)
drawing(65,200,37,0)
drawing(80,200,14,0)


hideturtle()
