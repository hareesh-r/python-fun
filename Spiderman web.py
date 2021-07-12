try:
    import turtle
except:
    import os
    os.system('pip -m install trutle')
    import turtle
    
har=turtle.Turtle()
w=turtle.Screen();w.bgcolor("black")
har.color("white");har.speed(8)
har.shape("square")
h=turtle.Turtle()
h.color("white");h.speed(8)
h.shape("circle")
k=60;u=90
h.setheading(270)
for i in range(200):
        har.fd(u)
        har.lt(k)
        u+=10
        k+=0.0
        h.fd(-u+5)
        h.lt(-k)
        if i%6==0:
                pass





