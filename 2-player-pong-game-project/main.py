import turtle
import block
import ball
import scoreboard
import time

block1 = block.Block((470, 0))
block2 = block.Block((-480, 0))
ball = ball.PongBall()

screen = turtle.Screen()
screen.bgcolor("Black")
screen.setup(width=1000, height=1000)
scoreboard1 = scoreboard.Scoreboard((-40, 350))
scoreboard2 = scoreboard.Scoreboard((40, 350))

screen.tracer(0)
screen.listen()
screen.onkey(block1.move_up, "Up")
screen.onkey(block1.move_down, "Down")
screen.onkey(block2.move_up, "w")
screen.onkey(block2.move_down, "s")

timmy = turtle.Turtle()
timmy.hideturtle()
timmy.penup()
timmy.pensize(5)
timmy.setheading(90)
timmy.pencolor("white")
timmy.goto(0, -360)

for i in range(36):
    if i % 2 == 0:
        timmy.pendown()
    else:
        timmy.penup()
    timmy.forward(20)

game_is_on = True
t = 0.05

while game_is_on:
    screen.update()
    time.sleep(t)
    ball.movement()
    if ball.ycor() > 360 or ball.ycor() < -360:
        ball.bounce_wall()
    if ball.xcor() > 450 or ball.xcor() < -460:
        if ball.distance(block1) < 50 or ball.distance(block2) < 50:
            ball.bounce_block()
            t *= 0.6
            if ball.xcor() > 0:
                scoreboard2.score += 1
                scoreboard2.score_update(scoreboard2.score)
            elif ball.xcor() < 0:
                scoreboard1.score += 1
                scoreboard1.score_update(scoreboard1.score)
        else:
            if ball.xcor() > 0:
                scoreboard1.score += 1
                scoreboard1.score_update(scoreboard1.score)
            else:
                scoreboard2.score += 1
                scoreboard2.score_update(scoreboard2.score)
            ball.bounce_block()
            t *= 0.9
            ball.goto(0, 0)

screen.exitonclick()
