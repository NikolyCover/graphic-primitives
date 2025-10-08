import turtle

INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

def compute_outcode(x, y, x_min, y_min, x_max, y_max):
    code = INSIDE 

    # 1º bit: y_max - y < 0  (ou seja, y > y_max)
    if y > y_max:
        code |= TOP

    # 2º bit: y - y_min < 0  (ou seja, y < y_min)
    if y < y_min:
        code |= BOTTOM

    # 3º bit: x_max - x < 0  (ou seja, x > x_max)
    if x > x_max:
        code |= RIGHT

    # 4º bit: x - x_min < 0  (ou seja, x < x_min)
    if x < x_min:
        code |= LEFT
        
    return code

def cohen_sutherland_clip(x1, y1, x2, y2, x_min, y_min, x_max, y_max):
    outcode1 = compute_outcode(x1, y1, x_min, y_min, x_max, y_max)
    outcode2 = compute_outcode(x2, y2, x_min, y_min, x_max, y_max)
    
    while True:
        # Aceite Trivial
        if not (outcode1 | outcode2):
            return True, x1, y1, x2, y2
        
        # Rejeite Trivial
        elif outcode1 & outcode2:
            return False, None, None, None, None
            
        # 3. Recorte necessário
        else:
            outcode_outside = outcode1 if outcode1 else outcode2
            
            # equação da reta: y = y1 + m * (x - x1)
            # m (inclinação) = (y2 - y1) / (x2 - x1)

            # x = x1 + (x2 - x1) * (y - y1) / (y2 - y1)
            # y = y1 + (y2 - y1) * (X - x1) / (x2 - x1)
            
            if outcode_outside & TOP:
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max
            elif outcode_outside & BOTTOM:
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min
            elif outcode_outside & RIGHT:
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max
            elif outcode_outside & LEFT:
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min
            
            if outcode_outside == outcode1:
                x1, y1 = x, y
                outcode1 = compute_outcode(x1, y1, x_min, y_min, x_max, y_max)
            else:
                x2, y2 = x, y
                outcode2 = compute_outcode(x2, y2, x_min, y_min, x_max, y_max)

def setup_environment(width=600, height=600):
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.title("Algoritmo de Cohen-Sutherland")
    screen.tracer(0)
    return screen

def draw_rectangle(t, x_min, y_min, x_max, y_max, color="blue"):
    t.pencolor(color)
    t.penup()
    t.goto(x_min, y_min)
    t.pendown()
    for _ in range(2):
        t.forward(x_max - x_min)
        t.left(90)
        t.forward(y_max - y_min)
        t.left(90)
    t.penup()

def draw_line(t, x1, y1, x2, y2, color="black"):
    t.pencolor(color)
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)
    t.penup()

def main():
    screen = setup_environment()
    t = turtle.Turtle()
    t.hideturtle()
    
    X_MIN, Y_MIN = -150, -100
    X_MAX, Y_MAX = 150, 100
    draw_rectangle(t, X_MIN, Y_MIN, X_MAX, Y_MAX, color="blue")

    test_lines = [
        ((-100, 50), (100, -50)),
        ((-250, 150), (-50, 150)),
        ((-200, -50), (200, 50)),
        ((50, -200), (50, 200)),
        ((0, 0), (-250, 75)),
        ((170, 120), (250, 200))
    ]

    for p1, p2 in test_lines:
        x1, y1 = p1
        x2, y2 = p2
        
        draw_line(t, x1, y1, x2, y2, color="lightgray")
        
        accepted, clip_x1, clip_y1, clip_x2, clip_y2 = cohen_sutherland_clip(
            x1, y1, x2, y2, X_MIN, Y_MIN, X_MAX, Y_MAX
        )
        
        if accepted:
            draw_line(t, clip_x1, clip_y1, clip_x2, clip_y2, color="green")

    screen.update()
    screen.exitonclick()

if __name__ == "__main__":
    main()