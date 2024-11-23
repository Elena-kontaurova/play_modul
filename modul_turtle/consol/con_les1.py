''' Рисуем фигупу по параметрам пользователя'''
import turtle

side = int(input('Введите количество сторон многоугольника: '))
size = int(input('Введите размер стороны многоугольника: '))
color = input('Введите цвет мноугольника: ')

t = turtle.Turtle()

angle = 360 / side


def polzovat(side, size):
    t.color(color)
    for _ in range(side):
        t.forward(size)
        t.left(angle)


polzovat(5, 200)
