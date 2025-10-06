import turtle

def move_without_drawing(t: turtle.Turtle, x: int, y: int):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_head(t: turtle.Turtle):
    move_without_drawing(t, 0, -100)
    t.color("black", "#D6A76A")  
    t.begin_fill()
    t.circle(100)
    t.end_fill()

def draw_ears(t: turtle.Turtle):
    # Left Ear
    move_without_drawing(t, -70, 75)
    t.color("black", "#CD853F")
    t.begin_fill()
    for _ in range(3):
        t.forward(50)
        t.left(120)
    t.end_fill()

    # Right Ear
    move_without_drawing(t, 20, 75)
    t.begin_fill()
    for _ in range(3):
        t.forward(50)
        t.left(120)
    t.end_fill()

def draw_eyes(t: turtle.Turtle):
    # Left Eye
    move_without_drawing(t, -30, 30)
    t.color("black", "black")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    # Right Eye
    move_without_drawing(t, 30, 30)
    t.begin_fill()
    t.circle(10)
    t.end_fill()

def draw_whiskers(t: turtle.Turtle):
    t.color("black")
    
    # Right Whiskers
    move_without_drawing(t, 10, 0)
    t.setheading(160)
    t.forward(40)

    move_without_drawing(t, 10, 0)
    t.setheading(180)
    t.forward(40)

    move_without_drawing(t, 10, 0)
    t.setheading(200)
    t.forward(40)

    # Left Whiskers
    move_without_drawing(t, -10, 0)
    t.setheading(20)
    t.forward(40)
    
    move_without_drawing(t, -10, 0)
    t.setheading(0)
    t.forward(40)
    
    move_without_drawing(t, -10, 0)
    t.setheading(-20)
    t.forward(40)

def draw_nose(t: turtle.Turtle):
    move_without_drawing(t, -12, 3)
    t.color("black", "pink")
    t.begin_fill()
    t.setheading(-90)
    t.circle(15, steps=3)  
    t.end_fill()

def draw_cat(t: turtle.Turtle):
    t.speed(10)
    t.pensize(3)
    
    draw_head(t)
    draw_ears(t)
    draw_eyes(t)
    draw_whiskers(t)
    draw_nose(t)
    
    t.hideturtle()