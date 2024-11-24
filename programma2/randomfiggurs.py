''' Фигуры рисуется по нажатию на экран
с рандомным цветом и формой'''
import turtle

import random

t = turtle.Turtle()
w = turtle.Screen()

t.speed(150)

colors = ['red', 'green', 'blue', 'orange', 'purple',
          'yellow', 'pink', 'cyan', 'magenta',
          'lime', 'teal', 'indigo']


def circle(x=t.xcor(), y=t.ycor()):
    ''' метод рисования солнышка'''
    radius = random.randint(50, 75)

    t.begin_fill()
    t.up()
    t.setposition(x, y)
    t.down()
    t.circle(radius)
    t.fillcolor(random.choice(colors))
    t.end_fill()

    x = t.xcor()
    y = t.ycor()

    for _ in range(50):
        t.up()
        t.setposition(x, y + radius)
        t.down()
        t.forward(radius + 45)
        t.right(360 / 50)


def zvezda(x=t.xcor(), y=t.ycor()):
    ''' jkjjj'''
    # radius = random.random(50, 75)
    t.begin_fill()
    t.up()
    t.setposition(x, y)
    t.down()
    t.fillcolor(random.choice(colors))

    x = t.xcor()
    y = t.ycor()

    for _ in range(5):
        t.forward(100)
        t.left(144)

    t.end_fill()


xs = ['circle', 'zvezda']


def move(a, b):
    ''' метод'''
    caca = random.choice(xs)
    if caca == 'circle':
        circle(x=a, y=b)
    if caca == 'zvezda':
        zvezda(x=a, y=b)


w.onclick(move)
w.listen()

turtle.done()
