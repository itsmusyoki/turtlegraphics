import turtle
from turtle import Turtle, Screen
import random

my_tut = Turtle()
my_tut.shape("turtle")
my_tut.color("blue")

colours = ["blue", "red", "yellow", "green"]
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        my_tut.forward(100)
        my_tut.right(angle)



for shape_sides in range(3, 11):
    draw_shape(shape_sides)
    my_tut.color(random.choice(colours))




screen = Screen()
screen.exitonclick()

