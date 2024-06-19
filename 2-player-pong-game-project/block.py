import turtle


class Block(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_len=4)
        self.goto(position)

    def move_up(self):
        if self.ycor() > -480 or self.ycor() < 480:
            self.setheading(90)
            self.forward(40)

    def move_down(self):
        if self.ycor() > -460 or self.ycor() < 460:
            self.setheading(90)
            self.backward(40)
