from turtle import Turtle
import random

colors = ["blue", "red", "yellow", "green", "black", "orange"]
directions = [0, 90, 180, 270]

tut = Turtle()
tut.shape("turtle")
tut.pensize(15)
tut.speed("fastest")

for _ in range(100):
    tut.forward(30)
    tut.setheading(random.choice(directions))
    tut.color(random.choice(colors))
