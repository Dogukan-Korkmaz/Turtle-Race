import turtle as t

scrn = t.Screen()
tim = t.Turtle()

tim.shapesize(2, 2, 2)
tim.shape("turtle")
tim.speed("fast")
tim.pensize(3)


def move_forward():
    tim.forward(40)

def move_backwars():
    tim.backward(80)

def counter_clockwise():
    new_heading = tim.heading() + 40
    tim.setheading(new_heading)

def clockwise():
    new_heading = tim.heading() - 40
    tim.setheading(new_heading)

def turn():
    tim.right(180)

def clear():
    tim.clear()

def home():
    tim.penup()
    tim.home()
    tim.pendown()



scrn.listen()
scrn.onkey(key="w", fun=move_forward)
scrn.onkey(move_backwars, "s")
scrn.onkey(counter_clockwise, "a")
scrn.onkey(clockwise, "d")
scrn.onkey(turn, "space")
scrn.onkey(clear, "c")
scrn.onkey(home, "h")





scrn.exitonclick()
