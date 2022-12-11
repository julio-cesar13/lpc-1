import turtle
import math

def fibonacci(n):
    a = 0
    b = 1
    square_a = a
    square_b = b

    tortoise.pencolor("orange")

    tortoise.fd(b * multiply)
    tortoise.lt(90)
    tortoise.fd(b * multiply)
    tortoise.lt(90)
    tortoise.fd(b * multiply)
    tortoise.lt(90)
    tortoise.fd(b * multiply)

    temp = square_b
    square_b = square_b + square_a
    square_a = temp

    for i in range(1, n):
        tortoise.bk(square_a * multiply)
        tortoise.rt(90)
        tortoise.fd(square_b * multiply)
        tortoise.lt(90)
        tortoise.fd(square_b * multiply)
        tortoise.lt(90)
        tortoise.fd(square_b * multiply)

        temp = square_b
        square_b = square_b + square_a
        square_a = temp

    tortoise.penup()
    tortoise.setposition(multiply, 0)
    tortoise.seth(0)
    tortoise.pendown()

    tortoise.pencolor("blue")

    tortoise.lt(90)
    for i in range(n):
        print(b)
        spirals = math.pi * b * multiply/2
        spirals /= 90
        for j in range(90):
            tortoise.fd(spirals)
            tortoise.lt(1)
        temp = a
        a = b
        b = temp + b

multiply = 5

n = int(input("escolha o número de repetições (> 1): "))

if n > 0:
    print(f"série de Fibonacci para {n} elementos: ")
    tortoise = turtle.Turtle()
    turtle.title("fibonacci spirals")
    tortoise.speed(100)
    fibonacci(n)
    turtle.done()
else:
    print("o número de repetições deve ser > 0.")