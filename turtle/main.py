from turtle import Turtle, Screen

tommy_the_turtle = Turtle()

tommy_the_turtle.shape("turtle")
tommy_the_turtle.color("red")


for _ in range(4):
    tommy_the_turtle.forward(100)
    tommy_the_turtle.right(90)

screen = Screen()
screen.exitonclick()