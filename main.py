from turtle import Turtle, Screen
from random import randint

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
my_turtles = []

screen = Screen()
screen.setup(width=500, height=500)

a = -240
b = 200
for _ in colors:
    new_turtle = Turtle("turtle")
    my_turtles.append(new_turtle)
    new_turtle.penup()
    new_turtle.color(_)
    new_turtle.setpos(x=-240, y= b)
    b -= 30

bet = screen.textinput(title="BET Enter", prompt="What turtle gonna win")

flag = False
if bet:
    flag = True

winner = ""
while flag:
    for turtle in my_turtles:
        random_distance = randint(0, 10)
        turtle.forward(random_distance)
        print(turtle.xcor())
        if turtle.xcor() >= 225:
            flag = False
            winner = turtle.pencolor()


if bet == winner:
    print(f"Right Guess, winner is {winner}")
else:
    print(f"Wrong Guess, winner is {winner}")

screen.exitonclick()
