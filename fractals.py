import math
import turtle

w = turtle.Screen()
size = w.screensize()
width = size[0]
print(width)
w.bgcolor("grey20")

t = turtle.Turtle()
t.hideturtle()
t.shape("turtle")
t.color("yellow")
t.pensize(2)
t.speed(0)

def koch(distance, level):
    if level == 0:
        t.forward(distance)
    else:
        koch(distance/3, level-1)
        t.left(60)
        koch(distance/3, level-1)
        t.right(120)
        koch(distance/3, level-1)
        t.left(60)
        koch(distance/3, level-1)


def koch_snowflake(distance, level):
    t.up()
    t.setpos(-distance/2, (-distance * math.sqrt(3))/4)
    t.down()
    for angle in [-60,120,120]:
        t.right(angle)
        koch(distance, level)
    t.setheading(0)

t.up()
t.backward(width/2)
t.down()
koch(width,3)

t.up()
t.setpos(0,0)
t.setheading(0)
t.down()
t.color("lightblue")
koch_snowflake(width,3)

w.exitonclick()
