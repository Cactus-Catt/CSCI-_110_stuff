'''notes 4-20 Turtle graphics'''

import turtle #library

scrn = turtle.Screen()
scrn.setup (800, 600) #screen size

turt = turtle.Turtle() #just a flash
turt.pencolor("red")
turt.pensize(5)
turt.forward(100)

turt2 = turtle.Turtle()
turt2.pencolor("blue")
turt2.pensize(5)
turt2.backward(100)


scrn.exitonclick() #needs to be last in the program


