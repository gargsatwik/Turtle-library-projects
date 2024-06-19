import turtle
import time
import car_manager
import scoreboard

timmy = turtle.Turtle("turtle")
screen = turtle.Screen()
car_manager = car_manager.Car()
scoreboard = scoreboard.Level()


def game_over():
    gameover = turtle.Turtle()
    gameover.hideturtle()
    gameover.penup()
    gameover.write("Game Over", False, "center", ("arial", 24, "bold"))


def move_forward():
    timmy.forward(10)


timmy.penup()
timmy.color("green")
timmy.goto(0, -280)
timmy.setheading(90)

screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(move_forward, "Up")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    car_manager.generate_cars()
    collision = car_manager.move_cars(timmy)
    if collision:
        game_is_on = False
        game_over()
    if timmy.ycor() > 300:
        timmy.goto(0, -280)
        scoreboard.update_level()
        car_manager.speed_up()
screen.exitonclick()
