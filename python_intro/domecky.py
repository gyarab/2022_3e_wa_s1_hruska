from turtle import *
import random
import math
t = Turtle()
shape("turtle")
speed(2)
def linka():
    forward(400)
    right(180)
    forward(800)
    penup()
    goto(0, 0)
    pendown()
    right(180)
    penup()
    goto(-350, 0)
    pendown()

linka()
def domek(a):
    left(90)
    forward(a)
    right(45)
    forward(a*math.sqrt(2)/2)
    right(90)
    forward(a*math.sqrt(2)/2)
    right(135)
    forward(a)
    left(135)
    forward(math.sqrt(2*a**2))
    left(135)
    forward(a)
    left(135)
    forward(math.sqrt(2*a**2))
    left(135)
    forward(a)

while True:
    domek(random.randint(25, 100))
    