''' Модуль Turtle'''
import turtle


def draw_cquare(color):
    ''' df'''
    t.begin_fill()
    t.color('green', color)
    for _ in range(3):
        t.forward(150)
        t.right(120)
    t.end_fill()


t = turtle.Turtle()

t.speed(130)

list_of_colors = ['indigo', 'brown', 'pink', 'purple']
for j in range(8):
    draw_cquare(list_of_colors[j % 4])
    t.right(45)
