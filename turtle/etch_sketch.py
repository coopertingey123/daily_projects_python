from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()



def move_forward():
    tim.forward(10)

def move_backward():
    tim.bk(10)

def clockwise():
    tim.right(2)

def counter_clockwise():
    tim.left(2)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=clockwise)
screen.onkeypress(key="d", fun=counter_clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()