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
    
    return None 


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
    
    return None


# ---------------------
# UCS
# ---------------------
def uniform_cost_search(start, goal, neighbors_fn):
    # TODO: Implement UCS Algorithm
    return None


# ---------------------
# A* Search
# ---------------------
def manhattan(a, b):
    # TODO: Implement Manhattan distance heuristic
    pass

def euclidean(a, b):
    # TODO: Implement Euclidean distance heuristic
    pass

def a_star_search(start, goal, neighbors_fn, heuristic="manhattan"):
    # TODO: Implement A* Algorithm
    return None