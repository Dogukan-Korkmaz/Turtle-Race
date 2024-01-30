import turtle as t

scrn = t.Screen()
scrn.setup(width=0.75, height=0.75, startx=None, starty=None)
tim = t.Turtle()

selected_turtle = scrn.textinput("Turtle Race!", "Please choise your turtle.")


scrn.exitonclick()