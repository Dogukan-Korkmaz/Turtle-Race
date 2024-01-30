import turtle as t

scrn = t.Screen()
tim = t.Turtle()

tim.shapesize(2, 2, 2)
tim.speed("fast")



def move_forward():
    t.right(90)
    t.forward(30)


scrn.onkey(key="space", fun=move_forward)
scrn.listen()



scrn.exitonclick()
