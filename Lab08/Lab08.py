import turtle
from turtle import Screen

t = turtle.Pen()
for x in range(80):
    t.forward(x * 1.5)
    t.left(91)

screen = Screen()
screen.exitonclick()
