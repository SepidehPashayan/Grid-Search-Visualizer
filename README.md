<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=220&section=header&text=Grid%20Search%20Visualizer&fontSize=54&fontAlignY=38&desc=Watch%20BFS%2C%20DFS%2C%20UCS%20and%20A*%20find%20their%20way%20through%20a%20living%20grid&descAlignY=60&descSize=17" alt="Grid Search Visualizer banner" width="100%"/>

<p>
  <img src="https://img.shields.io/badge/python-3.x-3776AB?logo=python&logoColor=white" alt="Python 3"/>
  <img src="https://img.shields.io/badge/pygame-2.x-00A86B?logo=python&logoColor=white" alt="Pygame 2"/>
  <img src="https://img.shields.io/badge/algorithms-BFS%20%7C%20DFS%20%7C%20UCS%20%7C%20A*-orange" alt="Algorithms"/>
</p>

**A Pygame playground for classic AI search algorithms.**
An agent navigates a randomly generated grid with obstacles, weighted terrain and *moving* obstacles. Watch it walk the path live, or benchmark every algorithm head to head.

</div>

---

## Table of contents

- [Overview](#-overview)
- [Features](#-features)
- [Demo](#-demo)
- [Algorithms at a glance](#-algorithms-at-a-glance)
- [Installation and usage](#-installation-and-usage)
- [Project structure](#-project-structure)
- [Notes](#-notes)
- [Author](#-author)

---

## 🧭 Overview

This project simulates an agent finding its way through a dynamic grid world using different search strategies. It has two modes:

- **Live visualization:** run one algorithm and watch the agent traverse the path it found.
- **Comparison mode:** benchmark all algorithms against each other on execution time, path length, nodes explored and path cost.

## ✨ Features

- 🗺️ Randomly generated grid with **fixed obstacles** and **weighted ("hard terrain") cells**
- 🚧 **Moving obstacles** that shift position at every step
- 🧠 Four search algorithms implemented from scratch:
  - **BFS**: Breadth-First Search
  - **DFS**: Depth-First Search
  - **UCS**: Uniform Cost Search
  - **A\*** with two heuristics: **Manhattan** and **Euclidean**
- 📊 **Comparison mode** reporting average runtime, path length, explored nodes and cost
- 🎬 Real-time graphical simulation of the agent moving along the computed path

## 🎬 Demo

> Add your own screenshots or a short GIF to `docs/` and they will show up here.

<div align="center">

| Live simulation | Algorithm comparison |
|:---:|:---:|
| <img src="docs/simulation.gif" alt="Agent walking along the found path" width="380"/> | <img src="docs/comparison.png" alt="Comparison of all algorithms" width="380"/> |

</div>

## 🧪 Algorithms at a glance

General, textbook properties of the algorithms used here (the comparison mode shows how they behave on *your* random grids):

| Algorithm | Uses cell costs | Typical behavior |
|---|:---:|---|
| **BFS** | no | Explores level by level, finds the path with the fewest steps |
| **DFS** | no | Goes deep first, often finds *a* path quickly but not the best one |
| **UCS** | yes | Always expands the cheapest node first, finds the lowest-cost path |
| **A\*** (Manhattan / Euclidean) | yes | Like UCS, but guided by a heuristic to explore fewer nodes |

## 🚀 Installation and usage

```bash
pip install pygame
python grid_env.py
```

Once it is running, choose from the menu:

1. Run a single algorithm with live visualization
2. Compare all algorithms
3. Exit

**Controls during the simulation:** `R` to restart, `ESC` to quit.

## 📁 Project structure

| File | Description |
|---|---|
| `search.py` | Search algorithm implementations (BFS, DFS, UCS, A\*) |
| `grid_env.py` | Grid environment, Pygame rendering and comparison logic |

## 📝 Notes

This project was built as part of an AI course assignment. All search algorithms in `search.py` were implemented by me. The initial skeleton of `grid_env.py` was provided by the course TA, and I modified and extended several parts of it.

## 👩‍💻 Author

**Sepideh Pashayan**

[![GitHub](https://img.shields.io/badge/GitHub-SepidehPashayan-181717?logo=github)](https://github.com/SepidehPashayan)

---

<div align="center">

If you enjoyed watching the algorithms race, consider giving it a ⭐

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=100&section=footer" alt="footer" width="100%"/>

</div>
