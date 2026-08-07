# Grid-Search-Visualizer

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-2.x-000000?style=flat&logo=python&logoColor=white)

A Pygame-based visualizer for classic search algorithms (BFS, DFS, UCS, A*) navigating a randomly generated grid world with obstacles, weighted terrain, and moving obstacles.

## Overview

This project simulates an agent finding its way through a dynamic grid environment using different search strategies. It includes a live visualization mode to watch the agent traverse the found path, as well as a comparison mode that benchmarks all algorithms against each other (execution time, path length, nodes explored, and path cost).

## Features

- Randomly generated grid with fixed obstacles and weighted ("hard terrain") cells
- Moving obstacles that shift position at every step
- Full implementation of four search algorithms:
  - **BFS** (Breadth-First Search)
  - **DFS** (Depth-First Search)
  - **UCS** (Uniform Cost Search)
  - **A\*** with two heuristics: Manhattan and Euclidean
- Algorithm comparison mode reporting average runtime, path length, explored nodes, and cost
- Real-time graphical simulation of the agent moving along the computed path

## Installation & Usage

\`\`\`bash
pip install pygame
python grid_env.py
\`\`\`

Once running, choose from the menu:
1. Run a single algorithm with live visualization
2. Compare all algorithms
3. Exit

Controls during simulation: \`R\` to restart, \`ESC\` to quit.

## Project Structure

| File | Description |
|---|---|
| \`search.py\` | Search algorithm implementations (BFS, DFS, UCS, A*) |
| \`grid_env.py\` | Grid environment, Pygame rendering, and comparison logic |

## Notes

This project was built as part of an AI course assignment. All search algorithms in \`search.py\` were implemented by me. The initial skeleton of \`grid_env.py\` was provided by the course TA, and I modified and extended several parts of it.

## Author

**Sepideh Pashayan**
