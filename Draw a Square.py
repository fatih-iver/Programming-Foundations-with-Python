import turtle, random

colors  = ["red","green","blue","orange","purple","pink","yellow"]

def draw_circle(Turtle):
    
    for i in range(360):
        color = random.choice(colors)
        Turtle.color(color)
        Turtle.forward(1)
        Turtle.left(1)        
        

def draw_triangle(Turtle):
    
    for i in range(3):
        color = random.choice(colors)
        Turtle.color(color)
        Turtle.forward(100)
        Turtle.left(120)        

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

Turtle2 = turtle.Turtle()
Turtle2.speed(0)
Turtle2.pensize(5)
Turtle2.shape("turtle")
Turtle2.color("green")


for i in range(24):
    draw_circle(Turtle)
    draw_triangle(Turtle)
    draw_square(Turtle)
    draw_square(Turtle2)
    Turtle.left(16)
    Turtle2.right(4)

Screen.exitonclick()


