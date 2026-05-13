# grid_env.py
# Random grid world with pygame visualization
# Obstacles, hard terrain, moving obstacles included
# After finishing the search 

import pygame
import random
import sys
import time
from search import depth_first_search, breadth_first_search, uniform_cost_search, a_star_search

#grid
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 15, 15
CELL_SIZE = WIDTH // COLS

#colors
WHITE = (255,255,255)
PINK = (255, 80, 80)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (139, 69, 19)
BLUE = (0, 0, 255)

#put 1 in all cell
#make empty road
def generate_grid():
    grid = [[1 for _ in range(COLS)] for _ in range(ROWS)]
    for _ in range(40):
        x, y = random.randrange(ROWS), random.randrange(COLS)
        grid[x][y] = None
    for _ in range(30):
        x, y = random.randrange(ROWS), random.randrange(COLS)
        if grid[x][y] == 1:
            grid[x][y] = 5
    return grid

#walls
def random_empty_cell(grid):
    while True:
        x, y = random.randrange(ROWS), random.randrange(COLS)
        if grid[x][y] is not None:
            return (x, y)
#??
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors_fn(grid, moving_obstacles, weighted=False):
    def neighbors(pos):
        x, y = pos
        results = []
        for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < ROWS and 0 <= ny < COLS:
                if grid[nx][ny] is not None and (nx, ny) not in moving_obstacles:
                    if weighted:
                        results.append(((nx, ny), grid[nx][ny]))  
                    else:
                        results.append((nx, ny))  
        return results
    return neighbors

#moving walls
def move_obstacles(moving_obstacles, grid):
    new_obs = set()
    for ox, oy in moving_obstacles:
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        random.shuffle(dirs)
        moved = False
        for dx, dy in dirs:
            nx, ny = ox+dx, oy+dy
            if 0 <= nx < ROWS and 0 <= ny < COLS and grid[nx][ny] is not None:
                new_obs.add((nx, ny))
                moved = True
                break
        if not moved:
            new_obs.add((ox, oy))
    return new_obs

#draw the grid with colors
def draw_grid(screen, grid, start, goal, current_pos, moving_obstacles):
    for x in range(ROWS):
        for y in range(COLS):
            center_x = y * CELL_SIZE + CELL_SIZE // 2
            center_y = x * CELL_SIZE + CELL_SIZE // 2
            radius = CELL_SIZE // 2 - 2
            if (x, y) == start:
                color = GREEN
            elif (x, y) == goal:
                color = RED
            elif (x, y) in moving_obstacles:
                color = BLUE
            elif grid[x][y] is None:
                color = BLACK
            elif grid[x][y] == 5:
                color = BROWN
            else:
                color = WHITE
            pygame.draw.circle(screen, color, (center_x, center_y), radius)
            pygame.draw.circle(screen, GREY, (center_x, center_y), radius, 1)

    # draw current agent position
    if current_pos:
        cx, cy = current_pos
        rect = pygame.Rect(cy*CELL_SIZE, cx*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, (0,255,255), rect)

def compare (start, goal, grid, moving_obstacles):
    algorithms = [
        ("BFS", lambda: breadth_first_search(start, goal, get_neighbors_fn(grid, moving_obstacles, weighted=False))),
        ("DFS", lambda: depth_first_search(start, goal, get_neighbors_fn(grid, moving_obstacles, weighted=False))),
        ("UCS", lambda: uniform_cost_search(start, goal, get_neighbors_fn(grid, moving_obstacles, weighted=True))),
        ("A* Manhattan", lambda: a_star_search(start, goal, get_neighbors_fn(grid, moving_obstacles, weighted=True), heuristic="manhattan")),
        ("A* Euclidean", lambda: a_star_search(start, goal, get_neighbors_fn(grid, moving_obstacles, weighted=True), heuristic="euclidean"))
    ]

    results = {} 

    for name, algo_func in algorithms:
        total_time = 0
        total_path_length = 0
        paths_found = 0
        exp = 0
        cost_all = 0
        for _ in range(5):
            start_time = time.time()
            if name == "DFS" or name == "BFS":
                path , explore = algo_func()
            else:
                path , explore , cost = algo_func()
                cost_all += cost
            end_time = time.time()
            exp += explore
            elapsed_time = end_time - start_time
            total_time += elapsed_time

            if path and isinstance(path, list) and len(path) > 0: 
                total_path_length += len(path) - 1
                paths_found += 1
            else:
                print(f"{name}: Path not found in this run.")

        avg_time = total_time / 5 if paths_found > 0 else 0
        avg_path = total_path_length / paths_found if paths_found > 0 else 0
        avg_exp = exp / 5
        avg_cost = cost_all / 5

        results[name] = {"avg_time": avg_time, "avg_path": avg_path}
        print(f"\n💛 {name} 💛")
        print(f"Average Time: {avg_time} seconds")
        print(f"Average Path Length: {avg_path}")
        print(f"Explored Nodes: {avg_exp}")
        if name == "UCS" or name == "A* Manhattan" or name == "A* Euclidean":
            print(f"Cost: {avg_cost}")


        



def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Search Algorithms with Obstacles")

    while True:  # outer loop for restart
        grid = generate_grid()
        start = random_empty_cell(grid)
        goal = random_empty_cell(grid)
        moving_obstacles = {(random.randrange(ROWS), random.randrange(COLS)) for _ in range(5)}

        print("\t💗Hi. welcome💗")
        print("\t💙what do you want to do ?💙")

        print("1:Try a strategy🧡")
        print("2.compare strategies🤍")
        print("3.exit 💙")
        x = input("Enter choice:")

        if x=="1":
            print("\nChoose algorithm:")
            print("1: DFS💛")
            print("2: BFS💜")
            print("3: UCS💚")
            print("4: A* (Manhattan)💗")
            print("5: A* (Euclidean)🤎")
            choice = input("Enter choice: ")

            path = None  
            result = None

            if choice == "1":  # DFS
                result = depth_first_search(start, goal, get_neighbors_fn(grid, moving_obstacles, weighted=False))
            elif choice == "2":  # BFS
                result = breadth_first_search(start, goal, get_neighbors_fn(grid, moving_obstacles, weighted=False))
            elif choice == "3":  # UCS
                result = uniform_cost_search(start, goal, get_neighbors_fn(grid, moving_obstacles, weighted=True))
            elif choice == "4":  # A* Manhattan
                result = a_star_search(start, goal, get_neighbors_fn(grid, moving_obstacles, weighted=True), heuristic="manhattan")
            elif choice == "5":  # A* Euclidean
                result = a_star_search(start, goal, get_neighbors_fn(grid, moving_obstacles, weighted=True), heuristic="euclidean")
            else:
                print(".....Invalid choice.....")
                continue


            if result:
                if isinstance(result, tuple) and len(result) >= 1:
                    path = result[0] 
                else: 
                    path = result
            
            print("path:")
            if isinstance(path, list):
                for item in path:
                    print(item)
            else:
                print("Path not found")


            step = 0
            clock = pygame.time.Clock()

            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:  # quit completely
                            pygame.quit()
                            sys.exit()
                        if event.key == pygame.K_r:  # restart
                            running = False

                moving_obstacles = move_obstacles(moving_obstacles, grid)

                screen.fill(PINK)
                current_pos = path[step] if path and step < len(path) else start
                draw_grid(screen, grid, start, goal, current_pos, moving_obstacles)
                pygame.display.flip()

                if path and step < len(path) - 1:
                    step += 1

                clock.tick(3)
        elif x=="2":
            compare(start,goal,grid, moving_obstacles)
        elif x=="3":
            pygame.quit()
            sys.exit()
        else:
            print(".....Invalid choice.....")


if __name__ == "__main__":
    main()
