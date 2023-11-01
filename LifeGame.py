import tkinter as tk
from tkinter import messagebox
import random
import copy

from GameMap import GameMap
from GameTimer import GameTimer

# MAX_HISTORY_LENGTH = 100
# MAX_REPEATED_STATES = 6

class LifeGame:
    def __init__(self, width, height, cell_size,root, canvas):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.root=root
        self.map = GameMap(width, height, cell_size, canvas)
        self.timer = GameTimer(self)
        self.stable = False
        self.history = []
        self.MAX_HISTORY_LENGTH = 100
        self.MAX_REPEATED_STATES = 6

    def update(self):
        grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        changed_cells = []  # 用于记录状态发生改变的细胞位置
        for y in range(self.map.height):
            for x in range(self.width):
                alive_neighbors = self.count_alive_neighbors(x, y)
                if self.map.grid[y][x] == 1:
                    if alive_neighbors < 2 or alive_neighbors > 3:
                        grid[y][x] = 0
                        changed_cells.append((x, y))  # 记录状态改变的细胞位置
                    else:
                        grid[y][x] = 1
                else:
                    if alive_neighbors == 3:
                        grid[y][x] = 1
                        changed_cells.append((x, y))  # 记录状态改变的细胞位置

        self.check_stable(grid)
        if self.stable:
            self.show_stable_message()
            self.timer.stop()
        else:
            self.map.grid = grid

        return changed_cells


    def check_stable(self, grid):
        self.history.append(grid)
        recent_history = self.history[-self.MAX_HISTORY_LENGTH:]
        if recent_history.count(grid) >= self.MAX_REPEATED_STATES:
            self.stable = True
        else:
            self.stable = False

    def show_stable_message(self):
            messagebox.showinfo("Message", "细胞状态已稳定。")
            self.timer.stop()

    def count_alive_neighbors(self, x, y):
        neighbors = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        alive_count = 0
        for dx, dy in neighbors:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height and self.map.grid[ny][nx] == 1:
                alive_count += 1
        return alive_count

    def clear(self):
        # self.map.clear_cells()
        # self.map = GameMap(self.width, self.height,self.cell_size,self.canvas)
        self.map.clear_cells()
        self.stable = False
        self.history = []

    def toggle_cells(self, event):
        self.map.toggle_cell(event)

