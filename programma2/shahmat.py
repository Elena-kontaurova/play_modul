''' Создаем шахватную доску'''
import turtle

t = turtle.Turtle()
square_size = 30

t.speed(150)

t.penup()
t.goto(-150, 150)
t.pendown()

color_list = ['white', 'black']


def draw_squeare():
    ''' Квадрат'''
    for _ in range(4):
        t.forward(square_size)
        t.right(90)


def draw_chess_board():
    ''' Полоса'''
    for col in range(8):
        for row in range(8):
            t.fillcolor(color_list[(col + row) % 2])
            t.begin_fill()
            draw_squeare()
            t.end_fill()
            t.forward(square_size)
        t.up()
        t.setposition(-150, - square_size * (col + 1) + 150)
        t.down()
    t.end_fill()


draw_chess_board()
turtle.done()
