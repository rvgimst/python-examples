import turtle

w = turtle.Screen()
w.bgcolor("grey20")

t = turtle.Turtle()
t.color("blue")
t.pensize(2)
t.speed(0)

def f(distance, level):
	if level == 0:
		t.forward(distance)
	else:
		f(distance/3, level-1)
		t.left(60)
		f(distance/3, level-1)
		t.right(120)
		f(distance/3, level-1)
		t.left(60)
		f(distance/3, level-1)

t.up()
t.backward(600)
t.down()

f(1200,5)
w.exitonclick()
