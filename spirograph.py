import turtle as t
import random

tut = t.Turtle()
tut.shape("turtle")
t.colormode(255)
tut.speed("fastest")

def change_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    random_color = (r,g,b)
    return random_color


def draw_spirograph(gap):
    for _ in range(int(360/ gap)):
        tut.color(change_color())
        tut.circle(100)
        tut.setheading(tut.heading() + gap)

draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()
