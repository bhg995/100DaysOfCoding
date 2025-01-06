import turtle
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_up():
    timmy.forward(10)


def move_down():
    timmy.backward(10)


def move_left():
    timmy.left(15)


def move_right():
    timmy.right(15)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
turtle.onkey(move_up, "Up")
turtle.onkey(move_down, "Down")
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(clear, "c")
screen.exitonclick()