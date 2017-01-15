import turtle
wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("darkgreen")


tess = turtle.Turtle()           # create tess and set some attributes
tess.color("white")
tess.pensize(5)

alex = turtle.Turtle()           # create alex
alex.color("blue")

tess.forward(80)                 # Let tess draw an equilateral triangle
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(160)
tess.left(120)                   # complete the triangle
tess.forward(80)
tess.left(120)                  # turn tess around
tess.forward(160)                 # move her away from the origin
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)

alex.forward(80)                 # make alex draw a square
alex.right(120)
alex.forward(80)
alex.right(120)
alex.forward(160)
alex.right(120)
alex.forward(80)
alex.right(120)
alex.forward(160)
alex.right(120)
alex.forward(80)
alex.right(120)
alex.forward(80)
wn.exitonclick()

