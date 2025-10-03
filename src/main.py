import turtle

tela = turtle.Screen()
tela.title("Lupitinha")
tela.bgcolor("#ADD8E6")

cat = turtle.Turtle()
cat.speed(5) 
cat.pensize(3)

def move(x, y):
    cat.penup()   
    cat.goto(x, y)  
    cat.pendown()

move(0, -100)
cat.color("black", "#FFDAB9")

cat.begin_fill() 
cat.circle(100) 
cat.end_fill()  