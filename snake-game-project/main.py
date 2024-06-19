import turtle
import time
import snake
import food
import scoreboard

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")

screen.tracer(0)
snake = snake.Snake()
food = food.Food()
scoreboard = scoreboard.Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    snake.reset()
    play_again = True
    scoreboard.clear()
    scoreboard.goto(0, 280)
    while play_again:
        screen.update()
        time.sleep(0.1)
        snake.move()
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.working()
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.high_score()
            play_again = False

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                play_again = False
                scoreboard.high_score()

screen.exitonclick()
