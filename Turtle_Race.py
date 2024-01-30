import turtle as t
import random

scrn = t.Screen()
scrn.colormode(255)
scrn.setup(width=0.75, height=0.75, startx=None, starty=None)

selected_turtle = scrn.textinput(title="Turtle Race!", prompt="Please choise your turtle.")

colors = ["red", "cyan", "black", "blue", "magenta", "white",
          "yellow", "silver", "pink", "gold", "grey", "aquamarine",
          "violet", "red3", "purple", "aqua", "lime", "gold3", "plum"]


def create_turtles(loc):
    racers = []
    for racer in range(10):
        racer = t.Turtle()
        racer.shape("turtle")
        r_choise = random.choice(colors)
        if r_choise == "":
            r_choise = random.choice(colors)
        racer.color(r_choise)
        colors.remove(r_choise)
        racer.shapesize(2, 2, 3)
        racer.penup()
        racer.goto(x=-600, y=loc)
        loc += 60
        racers.append(racer)
    return racers


def random_movement():
    turtles = create_turtles(-300)
    for _ in range(200):
        turtle = random.choice(turtles)
        turtle.forward(100)


random_movement()

scrn.exitonclick()
