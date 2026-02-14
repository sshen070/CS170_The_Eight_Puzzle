# 8-Puzzle Solver

## Overview

This project implements an 8-puzzle solver using three search algorithms:

- Uniform Cost Search (UCS)
- A* with Misplaced Tile heuristic
- A* with Manhattan Distance heuristic

The solver compares algorithm performance based on:
- Solution depth
- Nodes expanded
- Maximum queue size (memory usage)
- Execution time

---

## Algorithms

### 1. Uniform Cost Search (UCS)
- Expands nodes by lowest path cost `g(n)`
- No heuristic guidance
- Optimal and complete

### 2. A* (Misplaced Tile)
- `f(n) = g(n) + h(n)`
- `h(n)` = number of misplaced tiles
- More efficient than UCS

### 3. A* (Manhattan Distance)
- `f(n) = g(n) + h(n)`
- `h(n)` = sum of tile distances from goal position
- Most efficient in practice

---

## How to Run

```bash
python main.py
