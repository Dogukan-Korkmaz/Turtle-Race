import turtle as t
import random

scrn = t.Screen()
scrn.colormode(255)
scrn.setup(width=0.75, height=0.75, startx=None, starty=None)
scrn.title("Welcome To The Turtle Race!")

selected_turtle = scrn.textinput(title="Turtle Race!",
            prompt="Please choise your turtle:\n""""Red,Cyan,Black,Blue, Magenta,Yellow,Pink,Grey,Violet,Purple""")

colors = ["Red", "Cyan", "Black", "Blue", "Magenta",
          "Yellow", "Pink", "Grey",
          "Violet", "Purple"]


def create_turtles(loc):
    racers = []
    for racer in range(10):
        racer = t.Turtle()
        racer.shape("turtle")
        r_choise = random.choice(colors)
        racer.pen(pencolor=r_choise, pensize=3)
        racer.color(r_choise)
        colors.remove(r_choise)
        racer.shapesize(2, 2, 3)
        racer.penup()
        racer.goto(x=-600, y=loc)
        loc += 60
        racers.append(racer)
    return racers


def main_game():
    is_race_on = True
    turtles = create_turtles(-300)
    while is_race_on:
        r_move = random.randint(1, 30)
        turtle = random.choice(turtles)
        turtle.pendown()
        turtle.forward(r_move)
        if turtle.xcor() > 700:
            if turtle.pencolor() == selected_turtle.capitalize():
                print(f"{turtle.pencolor()} turtle wins ! Your bet was correct !")
            else:
                print(f"{turtle.pencolor()} turtle wins ! Your bet was incorrect !")
            scrn.bye()


main_game()

scrn.exitonclick()
