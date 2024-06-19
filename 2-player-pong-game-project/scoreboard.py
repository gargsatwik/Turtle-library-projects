import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.color("white")
        self.write("0", False, "center", ("Arial", 34, "bold"))
        self.hideturtle()
        self.score = 0

    def score_update(self, score):
        self.clear()
        self.write(f"{score}", False, "center", ("Arial", 34, "bold"))
