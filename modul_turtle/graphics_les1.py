''' Модуль Turtle'''
import turtle
import random

t = turtle.Turtle()


def square(pixels):
    ''' Рисуем квадрат'''
    for _ in range(4):
        t.forward(pixels)
        t.right(90)


t.speed(25)

list_colors = ['red', 'green', 'yellow', 'orange', 'pink']

initial_step = 30
for _ in range(60):
    t.color(random.choice(list_colors))
    t.right(10)
    square(initial_step)
    initial_step += 4
