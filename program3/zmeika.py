''' Игра змейка'''
import turtle

import random

w = turtle.Screen()
t = turtle.Turtle()
apple = turtle.Turtle()

t.shape('square')
t.color('black')
apple.shape('circle')
apple.color('red')
apple.penup()

apple.setposition(0, 200)
t.up()

current_direction = 'Right'


def moveUP():
    ''' Вверх'''
    global current_direction
    current_direction = 'Up'


def moveDOWN():
    ''' Вниз'''
    global current_direction
    current_direction = 'Down'


def moveLEFT():
    ''' Лево'''
    global current_direction
    current_direction = 'Left'


def moveRIGHT():
    ''' Право'''
    global current_direction
    current_direction = 'Right'


def isCollision(t1, t2):
    ''' дистанция'''
    distance = t1.distance(t2)
    return distance < 20


def checkCollision():
    ''' Перемещает яблоко'''
    if isCollision(t, apple):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        apple.setposition(x, y)


def move():
    ''' dfdf'''
    global current_direction
    checkCollision()

    if current_direction == 'Right':
        t.setx(t.xcor() + 10)

    elif current_direction == 'Left':
        t.setx(t.xcor() - 10)

    elif current_direction == 'Down':
        t.sety(t.ycor() - 10)

    elif current_direction == 'Up':
        t.sety(t.ycor() + 10)

    w.ontimer(move, 100)


w.onkey(moveRIGHT, 'Right')
w.onkey(moveDOWN, 'Down')
w.onkey(moveLEFT, 'Left')
w.onkey(moveUP, 'Up')

w.listen()

move()
w.mainloop()
