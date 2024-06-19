import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        with open("data.txt") as data:
            self.highest = int(data.read())
        self.goto(0, 280)
        self.write(f"Score: {self.score}", False, "center", ("Courier", 16, "bold"))

    def working(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}   High Score: {self.highest}", False, "center", ("Courier", 16, "bold"))

    def high_score(self):
        if self.score > self.highest:
            self.highest = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.highest))
        self.score = 0
