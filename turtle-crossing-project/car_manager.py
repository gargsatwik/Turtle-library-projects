import turtle
import random

y_coordinates = [-220, -180, -140, -100, -60, -20, 20, 60, 100, 140, 180, 220, 260]
colors = ["orange", "yellow", "green", "red", "brown", "blue"]


class Car(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.forward = 10
        self.cars = []

    def generate_cars(self):
        random_choice = random.randint(1, 6)
        if random_choice <= 2:
            new_car = turtle.Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2)
            new_car.color(random.choice(colors))
            new_car.goto(280, random.choice(y_coordinates))
            self.cars.append(new_car)

    def move_cars(self, tim):
        p = False
        for car in self.cars:
            car.backward(self.forward)
            if car.distance(tim) < 20:
                p = True
        return p

    def speed_up(self):
        self.forward += 1
