import turtle
from cat_drawer import draw_cat

def main():
    # 1. Desenhar gato
    screen = turtle.Screen()
    screen.title("Lupita")
    screen.bgcolor("#ADD8E6")

    cat_turtle = turtle.Turtle()

    draw_cat(cat_turtle)

    screen.mainloop()

if __name__ == "__main__":
    main()