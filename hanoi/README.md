# Tower of Hanoi – Python Project

## Overview

This project implements the classic Tower of Hanoi puzzle using Python. It combines a recursive algorithm, object-oriented programming, and a graphical user interface built with Pygame.

The goal is to move all disks from the starting tower to the target tower while following the rules of the puzzle.

## Rules

- Only one disk can be moved at a time.
- Only the top disk of a tower can be moved.
- A larger disk must never be placed on top of a smaller disk.

## Project Structure

- `scheibe.py` – Defines the disk objects and their sizes.
- `turm.py` – Implements the `Turm` class, which stores disks and checks whether a disk can legally be placed on a tower.
- `hanoi_solver.py` – Contains the recursive algorithm that determines the sequence of moves.
- `darstellung.py` – Implements the graphical representation and animation using Pygame.
- `main.py` – Creates the towers, initializes the puzzle, and starts the animation.

## Recursive Algorithm

The Tower of Hanoi algorithm solves the problem by breaking it down into smaller subproblems.

To move `n` disks from a starting tower to a target tower:

1. Move the top `n - 1` disks from the starting tower to the auxiliary tower.
2. Move the remaining largest disk to the target tower.
3. Move the `n - 1` disks from the auxiliary tower to the target tower.

The recursion stops when there are no disks left to move.

The minimum number of moves required to solve the puzzle with `n` disks is:

`2^n - 1`

For example, three disks require seven moves, while five disks require 31 moves.

## Object-Oriented Design

Each tower stores its disks in a Python list. The list is ordered from the bottom disk to the top disk.

- `append()` places a disk on top of a tower.
- `pop()` removes the top disk.
- `darf_ablegen()` checks whether a move respects the rules of the puzzle.

The `Turm` class encapsulates the tower's state and its placement rules. The solver is responsible for determining the correct sequence of moves.

## Animation and Callbacks

The graphical interface displays the three towers and their disks. After each move, the current state is redrawn.

The solver accepts an optional callback parameter called `nach_zug`. When a callback is provided, the solver calls it after each move.

In `main.py`, the function `aktualisiere()` is passed to the solver as this callback. It triggers the graphical update and introduces a short delay between moves.

This separates the recursive solving logic from the graphical representation. The solver does not need to know how Pygame draws the towers.

## Technologies

- Python
- Object-oriented programming (OOP)
- Recursion
- Pygame

## Purpose

This project is a learning exercise focused on recursion, classes and objects, separation of responsibilities, function callbacks, and basic graphical programming with Pygame.
