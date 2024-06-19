import turtle


class Level(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-230, 260)
        self.level = 1
        self.write(f"Level {self.level}", False, "center", ("Arial", 32, "bold"))

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", False, "center", ("Arial", 32, "bold"))
