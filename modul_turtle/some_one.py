''' Модуль Turtle'''

import turtle
import random

t = turtle.Turtle()


def hexagon(pixels):
    ''' Стоим типо шестиугольник'''
    for _ in range(6):
        t.forward(pixels)
        t.right(65)


t.speed(125)

list_colors = ['red', 'green', 'yellow', 'orange', 'pink']

init_step = 30
for _ in range(60):
    t.color(random.choice(list_colors))
    hexagon(init_step)
    init_step += 5
