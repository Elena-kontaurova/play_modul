''' Солнце'''
import turtle

import random

t = turtle.Turtle()
window = turtle.Screen()

t.speed(150)


def circle(x=t.xcor(), y=t.ycor()):
    ''' метод рисования солнышка'''
    radius = random.randint(50, 75)

    t.up()
    t.setposition(x, y)
    t.down()
    t.circle(radius)

    x = t.xcor()
    y = t.ycor()

    for _ in range(50):
        t.up()
        t.setposition(x, y + radius)
        t.down()
        t.forward(radius + 45)
        t.right(360 / 50)


def move(a, b):
    ''' метод'''
    circle(x=a, y=b)


window.onclick(move)
window.listen()

turtle.done()
