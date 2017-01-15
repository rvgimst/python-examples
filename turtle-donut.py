from turtle import *
from random import randint

width(3)
speed(0)

for i in range(200):
    x = randint(1, 8)
    if x == 1:
        color('purple')
    elif x == 2:
        color('blue')
    elif x == 3:
        color('red')
    elif x == 4:
        color('green')
    elif x == 5:
        color('orange')
    elif x == 6:
        color ('magenta')
    elif x == 7:
        color ('yellow')
    else:
        color('lightgreen')
    forward(300)
    right(123)

exitonclick()