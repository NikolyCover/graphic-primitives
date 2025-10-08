import turtle
import time

def setup_environment(width=600, height=600):
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.title("Polígonos")
    screen.setworldcoordinates(-50, -50, width - 50, height - 50)
    screen.tracer(0) 
    return screen

def draw_pixel(t: turtle.Turtle, x: int, y: int, color="white"):
    t.penup()
    t.goto(x, y)
    t.dot(3, color)

def midpoint_line_manual(t: turtle.Turtle, x1: int, y1: int, x2: int, y2: int, color="white"):

    x1, y1, x2, y2 = round(x1), round(y1), round(x2), round(y2)
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    step_x = 1 if x1 < x2 else -1
    step_y = 1 if y1 < y2 else -1
    
    x, y = x1, y1
    
    # Caso 1: A reta é mais "rasa" (variação em x é maior ou igual)
    if dx >= dy:
        d = 2 * dy - dx
        for _ in range(dx + 1):
            draw_pixel(t, x, y, color)
            if d > 0:
                y += step_y
                d += 2 * (dy - dx)
            else:
                d += 2 * dy
            x += step_x
            
    # Caso 2: A reta é mais "íngreme" (variação em y é maior)
    else:
        d = 2 * dx - dy
        for _ in range(dy + 1):
            draw_pixel(t, x, y, color)
            if d > 0:
                x += step_x
                d += 2 * (dx - dy)
            else:
                d += 2 * dx
            y += step_y

def draw_polygon_outline_manual(t: turtle.Turtle, vertices: list, color="white"):
    if len(vertices) < 2:
        return
        
    num_vertices = len(vertices)
    for i in range(num_vertices):
        start_point = vertices[i]
        end_point = vertices[(i + 1) % num_vertices]
        
        midpoint_line_manual(
            t,
            start_point[0], start_point[1],
            end_point[0], end_point[1],
            color=color
        )

def scanline_polygon_fill(t: turtle.Turtle, vertices: list, color="cyan"):
    if len(vertices) < 3: return
    edge_table = {}
    y_min_global, y_max_global = float('inf'), float('-inf')

    for i in range(len(vertices)):
        p1, p2 = vertices[i], vertices[(i + 1) % len(vertices)]
        y_min_global, y_max_global = min(y_min_global, p1[1], p2[1]), max(y_max_global, p1[1], p2[1])
        if p1[1] > p2[1]: p1, p2 = p2, p1
        if p1[1] == p2[1]: continue
        inverse_slope = (p2[0] - p1[0]) / (p2[1] - p1[1])
        y_min = round(p1[1])
        if y_min not in edge_table: edge_table[y_min] = []
        edge_table[y_min].append([round(p2[1]), p1[0], inverse_slope])

    active_edge_table = []
    for y in range(round(y_min_global), round(y_max_global) + 1):
        if y in edge_table: active_edge_table.extend(edge_table[y])
        active_edge_table = [edge for edge in active_edge_table if edge[0] > y]
        active_edge_table.sort(key=lambda edge: edge[1])
        for i in range(0, len(active_edge_table), 2):
            if i + 1 < len(active_edge_table):
                x_start, x_end = round(active_edge_table[i][1]), round(active_edge_table[i+1][1])
                for x in range(x_start, x_end + 1):
                    draw_pixel(t, x, y, color)
        for edge in active_edge_table: edge[1] += edge[2]

def main():
    screen = setup_environment(width=500, height=500)
    t = turtle.Turtle()
    t.hideturtle()

    star_polygon = [
        (250, 50), (288, 188), (425, 188), (325, 288),
        (362, 425), (250, 350), (138, 425), (175, 288),
        (75, 188), (212, 188)
    ]
    
    print("Iniciando preenchimento com Scan-Line...")
    start_time = time.time()
    scanline_polygon_fill(t, star_polygon, color="orange")
    screen.update()
    print(f"Preenchimento concluído em {time.time() - start_time:.2f} segundos.")

    print("Iniciando desenho do contorno com Algoritmo de Reta manual...")
    start_time = time.time()
    draw_polygon_outline_manual(t, star_polygon, color="red")
    screen.update()
    print(f"Contorno concluído em {time.time() - start_time:.2f} segundos.")
    
    print("Desenho finalizado. Clique na janela para sair.")
    screen.exitonclick()

if __name__ == "__main__":
    main()