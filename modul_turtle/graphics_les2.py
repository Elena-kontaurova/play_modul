''' Модуль Turtle'''
import turtle


def draw_cquare(color):
    ''' df'''
    t.begin_fill()
    t.color('red', color)
    for _ in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()


t = turtle.Turtle()

t.speed(130)

list_of_colors = ['green', 'yellow', 'orange', 'blue']
for j in range(8):
    draw_cquare(list_of_colors[j % 4])
    t.left(45)
