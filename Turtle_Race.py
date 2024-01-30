import turtle as t
import random

scrn = t.Screen()
scrn.colormode(255)
scrn.setup(width=0.75, height=0.75, startx=None, starty=None)

selected_turtle = scrn.textinput(title="Turtle Race!", prompt="Please choise your turtle.")


# def random_color():
#     r = random.randint(1, 255)
#     b = random.randint(1, 255)
#     g = random.randint(1, 255)
#     new_color = (r, b, g)
#     return new_color

colors = ["red", "cyan", "black", "blue", "magenta", "white",
          "yellow", "silver", "pink", "gold", "grey", "aguamarine",
          "violet", "red3", "purple", "aqua", "lime", "gold3", "plum"]


def create_turtles(loc):
    for x in range(10):
        x = t.Turtle()
        x.shape("turtle")
        r_choise = random.choice(colors)
        x.color(r_choise)
        colors.remove(r_choise)
        x.shapesize(2, 2, 3)
        x.penup()
        x.goto(x=-600, y=loc)
        loc += 60



create_turtles(-300)

scrn.exitonclick()