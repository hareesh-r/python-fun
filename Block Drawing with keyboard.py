import os
try:
    import turtle
except:
    os.system('pip -m install turtle')

try:
    import random
except:
    os.system('pip -m install random')

har = turtle.Turtle()
colours = ['red', 'blue', 'green', 'yellow', 'white', 'grey', 'pink']
shapes = ["triangle", "square", "circle", "arrow", "turtle"]
har.color(random.choices(colours))
har.width(6)

turtle.bgcolor('black')


def left():
    har.color(random.choices(colours))
    har.setheading(180)
    har.forward(100)


def right():
    har.color(random.choices(colours))
    har.setheading(0)
    har.forward(100)


def up():
    har.color(random.choices(colours))
    har.setheading(90)
    har.forward(100)


def down():
    har.color(random.choices(colours))
    har.setheading(270)
    har.forward(100)


def cr(x, y):
    har.shape(shapes[random.randrange(0, len(shapes))])
    har.stamp()


def cl(x, y):
    har.color(random.choices(colours))


turtle.listen()

turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')
turtle.onscreenclick(cl, 1)
turtle.onscreenclick(cr, 3)
turtle.mainloop()
