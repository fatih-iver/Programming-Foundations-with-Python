import turtle, random

colors  = ["red","green","blue","orange","purple","pink","yellow"]

def draw_triangle(Turtle):
    
    for i in range(3):
        #color = random.choice(colors)
        #Turtle.color(color)
        Turtle.forward(100)
        Turtle.left(120)
        
Screen = turtle.Screen()
Screen.bgcolor("black")
        
Turtle = turtle.Turtle()
Turtle.speed(0)
Turtle.pensize(1)
Turtle.color("white")
Turtle.hideturtle()

for i in range(24):
    rotate = i * 15 
    Turtle.home()
    Turtle.left(rotate)
    Turtle.color("white")
    Turtle.forward(50)
    draw_triangle(Turtle)
    
Screen.exitonclick()