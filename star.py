import turtle

# Create the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create the turtle
hex_turtle = turtle.Turtle()
hex_turtle.color("blue")
hex_turtle.pensize(3)
hex_turtle.speed(1)

n = 12
# Draw a hexagon (6 sides)
for _ in range(n):
    hex_turtle.forward(70)  # Move forward by 100 units
    hex_turtle.right(360/n)     # Turn 60 degrees (360° / 6 sides)

# Hide the turtle and display the window
hex_turtle.hideturtle()
turtle.done()
