import turtle as t
import random

# Function to draw a colorful star
def draw_colorful_star(size):
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    t.penup()
    t.goto(random.randint(-200, 200), random.randint(-200, 200))
    t.pendown()
    for _ in range(5):
        t.color(random.choice(colors))
        t.forward(size)
        t.right(144)

# Function to draw a colorful spiral
def draw_colorful_spiral(size, sides):
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    t.penup()
    t.goto(random.randint(-200, 200), random.randint(-200, 200))
    t.pendown()
    for _ in range(sides):
        t.color(random.choice(colors))
        t.forward(size)
        t.right(360 / sides)

# Set up the turtle
t.speed(0)
t.bgcolor("black")
t.hideturtle()

# Draw 20 colorful stars and spirals
for _ in range(20):
    draw_colorful_star(random.randint(50, 150))
    draw_colorful_spiral(random.randint(50, 150), random.randint(3, 8))

# Hide the turtle and display the result
t.hideturtle()
t.done()


