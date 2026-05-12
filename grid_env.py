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
WHITE = (255, 255, 255)
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
            rect = pygame.Rect(y*CELL_SIZE, x*CELL_SIZE, CELL_SIZE, CELL_SIZE)
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
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, GREY, rect, 1)

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
        for _ in range(5):
            start_time = time.time()
            path = algo_func()
            end_time = time.time()

            elapsed_time = end_time - start_time
            total_time += elapsed_time

            if path and path[0] != "path doesn't exist in":
                total_path_length += len(path) - 1
                paths_found += 1
            else:
                print(f"{name}: Path not found in this run.")

        avg_time = total_time / 5 if paths_found > 0 else 0
        avg_path = total_path_length / paths_found if paths_found > 0 else 0

        results[name] = {"avg_time": avg_time, "avg_path": avg_path}
        print(f"\n--- {name} ---")
        print(f"Average Time: {avg_time:.6f} seconds")
        print(f"Average Path Length: {avg_path:.2f}")

        



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
        x = input("Enter choice:")

        if x=="1":
            print("\nChoose algorithm:")
            print("1: DFS💛")
            print("2: BFS💜")
            print("3: UCS💚")
            print("4: A* (Manhattan)💗")
            print("5: A* (Euclidean)🤎")
            choice = input("Enter choice: ")

            if choice == "1":  # DFS
                algo = lambda s, g: depth_first_search(
                    s, g, get_neighbors_fn(grid, moving_obstacles, weighted=False)
                )
                print("path:")
                for item in depth_first_search(start, goal, get_neighbors_fn(grid, moving_obstacles, weighted=False)):
                    print(item)
            elif choice == "2":  # BFS
                algo = lambda s, g: breadth_first_search(
                    s, g, get_neighbors_fn(grid, moving_obstacles, weighted=False)
                )
                print("path:")
                for item in breadth_first_search(start, goal, get_neighbors_fn(grid, moving_obstacles, weighted=False)):
                    print(item)
            elif choice == "3":  # UCS
                algo = lambda s, g: uniform_cost_search(
                    s, g, get_neighbors_fn(grid, moving_obstacles, weighted=True)
                )
                print("path:")
                for item in uniform_cost_search(start, goal, get_neighbors_fn(grid, moving_obstacles, weighted=True)):
                    print(item)
            elif choice == "4":  # A* Manhattan
                algo = lambda s, g: a_star_search(
                    s, g, get_neighbors_fn(grid, moving_obstacles, weighted=True),
                    heuristic="manhattan"
                )
                print("path:")
                for item in a_star_search(start, goal, get_neighbors_fn(grid, moving_obstacles, weighted=True ), heuristic="manhattan"):
                    print(item)
            elif choice == "5":  # A* Euclidean
                algo = lambda s, g: a_star_search(
                    s, g, get_neighbors_fn(grid, moving_obstacles, weighted=True),
                    heuristic="euclidean"
                )
                print("path:")
                for item in a_star_search(start, goal, get_neighbors_fn(grid, moving_obstacles, weighted=True) , heuristic="euclidean" ):
                    print(item)
            else:
                print("Invalid choice")
                pygame.quit()
                sys.exit()


            path = algo(start, goal)
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

                screen.fill(WHITE)
                current_pos = path[step] if path and step < len(path) else start
                draw_grid(screen, grid, start, goal, current_pos, moving_obstacles)
                pygame.display.flip()

                if path and step < len(path) - 1:
                    step += 1

                clock.tick(3)
        elif x=="2":
            compare(start,goal,grid, moving_obstacles)
        else:
            print("Invalid choice")
        #if x=="1":


if __name__ == "__main__":
    main()
