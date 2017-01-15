from turtle import *
speed(0)
#color('red', 'yellow')
begin_fill()
while True:
    forward(400)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()