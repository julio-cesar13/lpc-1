import turtle

screen = turtle.getscreen()
tortoise = turtle.Turtle()
tortoise.color("orange", "white")

def triangle(x , y):
    tortoise.penup()
    tortoise.goto(x, y)
    tortoise.pendown()
    for i in range(3):
        tortoise.fd(60)
        tortoise.lt(120)
        tortoise.fd(60)

turtle.onscreenclick(triangle, 1)
turtle.listen()

turtle.done()
