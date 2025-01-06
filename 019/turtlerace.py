from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Step right up", prompt="Which lucky winner ya pickin? ")
colors = [
    "indigo", "green", "orange", "red", "brown", "gray",
]
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []

for turtle in range(len(y_positions)):
    turtle_new = Turtle(shape="turtle")
    turtle_new.color(colors[turtle])
    turtle_new.penup()
    turtle_new.goto(x=-220, y=y_positions[turtle])
    turtles.append(turtle_new)


if user_bet:
    racing = True

while racing:

    for turtle in turtles:
        if turtle.xcor() > 220:
            racing = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won. Da winner: '{winning_color}'")
            else:
                print(f"You lost. Da winner '{winning_color}'")

        rand_steps = random.randint(0, 10)
        turtle.forward(rand_steps)

screen.exitonclick()