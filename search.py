"""
search.py

Students must implement TODO sections.
Includes: BFS, DFS, UCS, A* (with Manhattan & Euclidean heuristics).
"""

from collections import deque
import heapq
import math


# ---------------------
# BFS
# ---------------------
def breadth_first_search(start, goal, neighbors_fn):
    # TODO: Implement BFS Algorithm
    fringe=deque([start])
    explored={start}
    parent = {start: None}

    while fringe:
        current_node = fringe.popleft()
        if current_node == goal:
            path = []
            node = goal
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]
    
        for neighbor in neighbors_fn(current_node):
              if neighbor not in explored:
                   explored.add(neighbor)
                   parent[neighbor] = current_node
                   fringe.append(neighbor)
    
    return None , path


# ---------------------
# DFS
# ---------------------
def depth_first_search(start, goal, neighbors_fn):
    # TODO: Implement DFS Algorithm
    fringe=deque([start])
    explored={start}
    parent = {start: None}

    while fringe:
        current_node = fringe.pop()
        if current_node == goal:
            path = []
            node = goal
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]
    
        for neighbor in neighbors_fn(current_node):
              if neighbor not in explored:
                   explored.add(neighbor)
                   parent[neighbor] = current_node
                   fringe.append(neighbor)
    
    return None , path


# ---------------------
# UCS
# ---------------------
def uniform_cost_search(start, goal, neighbors_fn):
    # TODO: Implement UCS Algorithm
    fringe = [(0, start)]
    explored_costs = {start: 0}
    parent = {start: None}

    while fringe:
        cost, current_node = heapq.heappop(fringe)
        if cost > explored_costs.get(current_node, float('inf')):
            continue
        if current_node == goal:
            path = []
            node = goal
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]
    
        for neighbor, step_cost in neighbors_fn(current_node):
            new_cost = cost + step_cost
            if new_cost < explored_costs.get(neighbor, float('inf')):
                parent[neighbor] = current_node
                explored_costs[neighbor] = new_cost
                heapq.heappush(fringe, (new_cost, neighbor))
    
    return None , path


# ---------------------
# A* Search
# ---------------------
def manhattan(a, b):
    # TODO: Implement Manhattan distance heuristic
    xa , ya = a
    xb , yb = b
    return abs(xb-xa) + abs(yb-ya)

def euclidean(a, b):
    # TODO: Implement Euclidean distance heuristic
    xa , ya = a
    xb , yb = b
    return math.sqrt((yb-ya)**2 + (xb-xa)**2)

def a_star_search(start, goal, neighbors_fn, heuristic):
    # TODO: Implement A* Algorithm
    if heuristic == "manhattan":
        h_start = manhattan(start, goal)
    else:
        h_start = euclidean(start, goal)
        
    fringe = [(h_start, 0, start)]  
    
    explored_costs = {start: 0}
    
    parent = {start: None}

    while fringe:
        f_cost, current_g_cost, current_node = heapq.heappop(fringe)
        if current_g_cost > explored_costs.get(current_node, float('inf')):
            continue
        if current_node == goal:
            path = []
            node = goal
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]

        for neighbor, step_cost in neighbors_fn(current_node):
            new_g_cost = current_g_cost + step_cost
            if new_g_cost < explored_costs.get(neighbor, float('inf')):
                explored_costs[neighbor] = new_g_cost
                if heuristic == "manhattan":
                    h_neighbor = manhattan(neighbor, goal)
                else: 
                    h_neighbor = euclidean(neighbor, goal)

                new_f_cost = new_g_cost + h_neighbor

                heapq.heappush(fringe, (new_f_cost, new_g_cost, neighbor))
                parent[neighbor] = current_node

    return None , path