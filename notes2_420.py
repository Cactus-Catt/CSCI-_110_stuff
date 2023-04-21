import turtle

scrn=turtle.Screen()
scrn.setup (800, 600)

turt = turtle.Turtle()

turt.penup() #draw sky
turt.pensize(5)
turt.pencolor ("blue")
turt.fillcolor ("blue")
turt.goto (-400, 300)
turt.pendown()
turt.begin_fill()
turt.forward (800)
turt.right (90)
turt.forward (300)
turt.right (90)
turt.forward (300)
turt.forward (800)
turt.right (90)
turt.forward (300)


turt.end_fill()

#draw the grass
turt.penup()
turt.goto (-400, 0)
turt.pencolor ("green")
turt.fillcolor ("green")
turt.pensize(5)

turt.pendown()
turt.begin_fill()
turt.forward (800)
turt.right (90)
turt.forward (300)
turt.right (90)
turt.forward (300)
turt.forward (800)
turt.right (90)
turt.forward (300)
turt.end_fill()

turt.fillcolor ("yellow")
turt.begin_fill()
turt.circle(50)
turt.end_fill

scrn.exitonclick()