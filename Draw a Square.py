import turtle, random

colors  = ["red","green","blue","orange","purple","pink","yellow"]

def draw_square(Turtle):
    
    for i in range(4):
        color = random.choice(colors)
        Turtle.color(color)
        Turtle.forward(100)
        Turtle.right(90)
    
Screen = turtle.Screen()
Screen.bgcolor("black")

Turtle = turtle.Turtle()
Turtle.speed(0)
Turtle.pensize(5)
Turtle.shape("turtle")
Turtle.color("green")


for i in range(24):
    draw_square(Turtle)
    Turtle.left(15)

Screen.exitonclick()


