#simplified code
from turtle import *
import random
angle_lst = [105,75,15,-55,-135,-50]
fwd = [200,50,20,35,120,40]
color("red")
begin_fill()
pensize(4)
c=0
title("Tesla")
begin_fill()
for i in range(2):
    up()
    goto(0,-100)
    down()
    if(i==1):
        left(180-angle_lst[0]) #for symmetry first one is 180-angle
        for j in range(5):
            j+=1
            angle_lst[j] *= -1 #change angle directions      
    else:
        left(angle_lst[c])
    c+=1
    for k in range(5):
        
        fd(fwd[k])
        left(angle_lst[c])
        c+=1
    c=0
    fd(40)
    left(45)
hideturtle()
end_fill()


























'''
from turtle import *
import random
angle_lst = [105,75,15,-55,-135,-50]
color("red")
begin_fill()
pensize(4)
c=0
title("Tesla")
for i in range(2):
    up()
    goto(0,-100)
    down()
    if(i==1):
        left(180-angle_lst[0])
        for j in range(5):
            j+=1
            angle_lst[j] *= -1
            
    else:
        left(angle_lst[c])
    c+=1    
    fd(200)
    left(angle_lst[c])
    c+=1
    fd(50)
    left(angle_lst[c])
    c+=1
    fd(20)
    left(angle_lst[c])
    c+=1
    fd(35)

    left(angle_lst[c])
    c+=1
    fd(120)
    left(angle_lst[c])
    c=0
    fd(40)
    left(45)

end_fill()
hideturtle()


'''    
