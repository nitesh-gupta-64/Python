import turtle

t = turtle.Turtle()

t.fillcolor("red")
t.pensize(2)

t.begin_fill()
t.circle(50)

t.end_fill()

t.penup()
t.goto(0, 10)
t.pendown()

t.fillcolor("red")
t.begin_fill()
t.circle(40)
t.end_fill()

t.hideturtle()

turtle.done()
