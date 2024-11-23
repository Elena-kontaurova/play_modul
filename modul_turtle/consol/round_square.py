''' Создаем круг из квадратов'''
import turtle

t = turtle.Turtle()


def square(size):
    ''' рири'''
    for _ in range(5):
        t.forward(size)
        t.left(90)


t.speed(120)

t.penup()
t.goto(-150, 150)
t.pendown()

colors = ['red', 'green', 'blue', 'orange', 'purple',
          'yellow', 'pink', 'cyan', 'magenta',
          'lime', 'teal', 'indigo']

side_lenth = 75
for _ in range(12):
    t.begin_fill()
    t.fillcolor(colors[_ % len(colors)])
    square(side_lenth)
    t.right(120)
    t.end_fill()
