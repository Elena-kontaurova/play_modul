''' kbhh'''
import turtle

import random


t = turtle.Turtle()

colors = ['red', 'orange', 'yellow',
          'green', 'blue', 'purple']

shapes = ['triangle', 'square']

t.speed(130)


def draw_squeare(size):
    ''' hghg'''
    t.begin_fill()
    for _ in range(4):
        t.fillcolor(random.choice(colors))
        t.forward(size)
        t.left(90)
    t.end_fill()


t.penup()
t.goto(-250, -100)
t.pendown()


def draw_triangle(size):
    ''' hggh'''
    t.begin_fill()
    for _ in range(3):
        t.fillcolor(random.choice(colors))
        t.forward(size)
        t.left(120)
    t.end_fill()


for _ in range(100):
    shape = random.choice(shapes)
    size = random.randint(100, 400)
    if shape == 'triangle':
        draw_triangle(size)
    elif shape == 'square':
        draw_squeare(size)
