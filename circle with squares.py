import turtle
import random
clr=["red","white","blue","cyan","orange","brown","green","yellow"]
turtle.bgcolor('black')
turtle.width(5)
turtle.speed(9)
for i in range(6):
    for j in range(10):
        turtle.color(random.choices(clr))
        turtle.lt(12)
        turtle.fd(200)
        turtle.lt(90)
        turtle.fd(200)
        turtle.lt(90)
        turtle.fd(200)
        turtle.lt(90)
        turtle.fd(200)
        turtle.lt(90)

