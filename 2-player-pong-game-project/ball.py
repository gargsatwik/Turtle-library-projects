import turtle
import random

directions = [45, 135, 225, 315]


class PongBall(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.setheading(random.choice(directions))
        self.speed("fastest")
        self.x_move = 10
        self.y_move = 10

    def movement(self):
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_block(self):
        self.x_move *= -1
