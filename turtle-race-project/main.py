import turtle
import random

is_race_on = False
colors = ["red", "green", "blue", "orange", "yellow", "brown"]
screen = turtle.Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

if user_input:
    is_race_on = True

turtles = []

for i in range(6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-230, -100 + i * 40)
    turtles.append(new_turtle)

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

if winner.lower() == user_input.lower():
    print(f"You've won. The {winner} turtle is the winner!")
else:
    print(f"You've lost. The {winner} turtle is the winner!")

screen.bye()
# screen.exitonclick()
