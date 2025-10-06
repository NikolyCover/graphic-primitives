import turtle

def setup_environment(width=600, height=600, bgcolor="black"):
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.title("Algoritmo do Ponto Médio para Retas")
    screen.bgcolor(bgcolor)

    # Coloca a origem (0,0) no canto inferior esquerdo
    screen.setworldcoordinates(-50, -50, width - 50, height - 50)

    screen.tracer(0)
    
    pixel_drawer = turtle.Turtle()
    pixel_drawer.hideturtle()
    pixel_drawer.speed(10)
    pixel_drawer.penup()
    
    return screen, pixel_drawer

def draw_pixel(t: turtle.Turtle, x: int, y: int, color="white"):
    t.goto(x, y)
    t.dot(4, color) 

def midpoint_line(t: turtle.Turtle, x1: int, y1: int, x2: int, y2: int, color="cyan"):
    dx = x2 - x1
    dy = y2 - y1
    
    # Parâmetro de decisão inicial. Multiplicamos por 2 para evitar floats.
    d = 2 * dy - dx
    
    increment_E = 2 * dy      
    increment_NE = 2 * (dy - dx)

    x, y = x1, y1
    draw_pixel(t, x, y, color)
    
    while x < x2:
        x += 1

        # Se d < 0, a linha está abaixo do ponto médio
        if d <= 0:
            d += increment_E

        # Se d > 0, a linha está acima do ponto médio
        else:
            d += increment_NE
            y += 1
            
        draw_pixel(t, x, y, color)

def main():
    screen, pixel_drawer = setup_environment(width=500, height=500)
    
    print("Desenhando linhas com o Algoritmo do Ponto Médio...")
    
    # Exemplo 1: Reta com inclinação baixa
    midpoint_line(pixel_drawer, 0, 0, 400, 100, color="yellow")
    
    # Exemplo 2: Reta com inclinação próxima de 1 (45 graus)
    midpoint_line(pixel_drawer, 0, 50, 300, 350, color="magenta")
    
    # Exemplo 3: Reta horizontal (caso especial)
    midpoint_line(pixel_drawer, 50, 400, 450, 400, color="lime")
    
    # Exemplo 4: Reta curta
    midpoint_line(pixel_drawer, 20, 250, 150, 300, color="cyan")
    
    screen.update()
    print("Desenho concluído. Clique na janela para sair.")
    screen.exitonclick()

if __name__ == "__main__":
    main()