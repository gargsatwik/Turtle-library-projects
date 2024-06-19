import turtle

timmy = turtle.Turtle()
screen = turtle.Screen()


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def rotate_right():
    # timmy.setheading(timmy.heading()+10)
    timmy.right(10)


def rotate_left():
    # timmy.setheading(timmy.heading()-10)
    timmy.left(10)


def clear_screen():
    timmy.reset()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=rotate_left)
screen.onkey(key="d", fun=rotate_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
