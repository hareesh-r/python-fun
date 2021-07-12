try:
    import turtle
except:
    import os
    os.system('pip -m install trutle')
    import turtle    

screen= turtle.Screen()

har=turtle.Turtle()
har.speed(-1)

def drag(x,y):
    har.ondrag(None)
    har.setheading(har.towards(x,y))
    har.goto(x,y)
    har.ondrag(drag)

def cr(x,y):
    har.clear()

def main():
    turtle.listen()

    har.ondrag(drag)

    turtle.onscreenclick(cr,3)

    screen.mainloop()
main()

