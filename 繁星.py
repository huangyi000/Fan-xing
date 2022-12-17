import turtle as t
t.speed(0)
#bg=background缩写

t.bgcolor('black')

t.colormode(255)

t.pensize(100)
t.color(25,25,25)
t.penup()
t.goto(-800,250)
t.pendown()
t.forward(1600)

t.pensize(100)
t.color(50,50,50)
t.penup()
t.goto(-750,150)
t.pendown()
t.forward(1600)

t.pensize(100)
t.color(75,75,75)
t.penup()
t.goto(-800,50)
t.pendown()
t.forward(1600)

t.pensize(100)
t.color(100,100,100)
t.penup()
t.goto(-800,-50)
t.pendown()
t.forward(1600)


t.pensize(100)
t.color(125,125,125)
t.penup()
t.goto(-800,-150)
t.pendown()
t.forward(1600)

t.pensize(100)
t.color(150,150,150)
t.penup()
t.goto(-800,-250)
t.pendown()
t.forward(1600)

t.pensize(100)
t.color(175,175,175)
t.penup()
t.goto(-800,-350)
t.pendown()
t.forward(1600)

#星星
import random

t.pensize(1)
for x in range(20):
    x=random.randint(-800,800)
    y=random.randint(0,350)

    t.color("yellow")

    t.penup()
    t.goto(x,y)
    t.pendown()

    l=random.randint(15,30)

    t.begin_fill()
    t.left(30)
    for i in range(8):
        t.forward(l)
        t.left(30)
        t.forward(l)
        t.right(120)
    t.end_fill()
