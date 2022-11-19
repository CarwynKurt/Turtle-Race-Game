# Turtle Race
# 1. Import
import turtle
import time

from turtle import Turtle
from random import randint

# 2. Design Grass
screen = turtle.Screen()
tr=Turtle()

screen.bgcolor("forestgreen")
tr.color("white")
tr.speed(0)
tr.penup()
tr.goto(-120, 280)
tr.write("TURTLE RACE", font=("Times New Roman", 20, "bold"))
tr.penup()

# 3. Design Soil
tr.goto(-400, -279)
tr. color("chocolate")
tr.begin_fill()
tr.pendown()
tr.forward(700)
tr.right(90)
tr.forward(700)
tr.end_fill()

# 4. Design Finish Line
square_size = 20
finish_line = 300

tr.color("black")
tr.shape("square")
tr.penup()

for i in range(14):
    tr.goto(finish_line, (260 - (i * square_size * 2)))
    tr.stamp()

for j in range(13):
    tr.goto(finish_line + square_size, ((260 - square_size) - (j * square_size * 2)))
    tr.stamp()

# 5. Input Racer 1
racer1 = Turtle()
racer1.speed(0)
racer1.color("red")
racer1.shape("turtle")
racer1.turtlesize(3)
racer1.penup()
racer1.goto(-400, 200)
racer1.pendown()

# 6. Input Racer 2
# 7. Input Racer 3
# 8. Input Racer 4
# 9. Move the Turtle
# 10 Setup Winner
# 11 Monitor Distance
# 12 Display the winner


turtle.done()