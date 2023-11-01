import tkinter as tk
from tkinter import messagebox
import random
import copy

class GameMap:
    def __init__(self, width, height, cell_size, Canvas):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.canvas = Canvas
        # self.canvas.bind("<Button-1>", lambda event: self.toggle_cell(event))
        self.can_wid = Canvas.winfo_width()
        self.can_hei = Canvas.winfo_height()
        self.grid = [[0 for _ in range(width)] for _ in range(height)]

    def toggle_cell(self, event):
        x = event.x // self.cell_size
        y = event.y // self.cell_size
        self.grid[y][x] = 1 - self.grid[y][x]
        self.draw_cells()

    def randomize_cells(self, density):
        for y in range(self.height):
            for x in range(self.width):
                self.grid[y][x] = 1 if random.random() < density else 0
        self.draw_cells()

    def clear_cells(self):
        for y in range(self.height):
            for x in range(self.width):
                self.grid[y][x] = 0

        self.canvas.delete("all")
        self.draw_grid()

    def draw_grid(self):
        for x in range(0, 700, self.cell_size):
            self.canvas.create_line(x, 0, x, 700, fill="black")
        for y in range(0, 700, self.cell_size):
            self.canvas.create_line(0, y, 700, y, fill="black")

        for x in range(0, 700, self.cell_size):
            for y in range(0, 700, self.cell_size):
                self.canvas.create_rectangle(x, y, x + self.cell_size, y + self.cell_size, fill="white")

    def draw_cells(self):
        for y in range(self.height):
            for x in range(self.width):
                fill_color = "black" if self.grid[y][x] == 1 else "white"
                self.canvas.create_rectangle(
                    x * self.cell_size,
                    y * self.cell_size,
                    (x + 1) * self.cell_size,
                    (y + 1) * self.cell_size,
                    fill=fill_color
                )


    def draw_changed_cells(self, changed_cells):
        for x, y in changed_cells:
            fill_color = "black" if self.grid[y][x] == 1 else "white"
            self.canvas.create_rectangle(
                x * self.cell_size,
                y * self.cell_size,
                (x + 1) * self.cell_size,
                (y + 1) * self.cell_size,
                fill=fill_color
            )
