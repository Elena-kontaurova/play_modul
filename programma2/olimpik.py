''' Программа отрисовки олимпийских колец'''
import turtle

window = turtle.Screen()

turtles = [turtle.Turtle() for _ in range(5)]

for i in turtles:
    i.up()

turtles[0].goto(-100, 100)
turtles[1].goto(0, 100)
turtles[2].goto(100, 100)
turtles[3].goto(-50, 50)
turtles[4].goto(50, 50)

list_color = ['blue', 'black', 'red', 'yellow', 'green']

for i, tur in enumerate(turtles):
    tur.down()
    tur.color(list_color[i])
    tur.pensize(15)
    tur.circle(50)

window.mainloop()
