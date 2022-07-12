# import turtle
# import random
# from random import randint
# t = turtle.Turtle()
# list1 = ['yellow', 'red', 'blue', 'black']
# t.up()
# t.goto(200, 0)
# for i in range(4):
#     t.down()
#     t.begin_fill()
#     t.fillcolor(randint(0,255), randint(0, 255), randint(0, 255))
#     t.circle(50)
#     t.end_fill()
#     t.up()
#     t.bk(100)
from turtle import *
from random import randint
import math
speed(0)
pensize(5)
colormode(255)
k = int(input())
for i in range(k):
    color(randint(0, 255),
          randint(0, 255),
          randint(0, 255))
    begin_fill()
    circle(50)
    end_fill()
    penup()
    x = (10 + 2*i)*math.cos(i)
    y = (10 + 2*i)*math.sin(i)
    goto(x, y)
    pendown()

