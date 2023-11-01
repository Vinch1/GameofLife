import tkinter as tk
from tkinter import messagebox
import random
import copy

from LifeGame import LifeGame

root = tk.Tk()
CAnvas = tk.Canvas(root, width=700, height=700,bg="white", borderwidth=2, relief="solid")
CAnvas.grid(row=0, column=0, columnspan=2)
life_game = LifeGame(width=50, height=50, cell_size=18,root=root, canvas=CAnvas)
life_game.map.draw_grid()


def Set_UI():
    root.title("生命游戏")
    button_frame = tk.Frame(root)
    button_frame.grid(row=0, column=2, rowspan=5)

    start_button = tk.Button(button_frame, text="开始", command=life_game.timer.start)
    start_button.grid(row=0, column=0, pady=5)

    stop_button = tk.Button(button_frame, text="停止", command=life_game.timer.stop)
    stop_button.grid(row=1, column=0, pady=5)

    random_density = tk.DoubleVar()
    density_label = tk.Label(button_frame, text="细胞密度 (0.0 - 1.0)")
    density_label.grid(row=2, column=0, pady=5)
    density_entry = tk.Entry(button_frame, textvariable=random_density)
    density_entry.grid(row=3, column=0, pady=5)
    randomize_button = tk.Button(button_frame, text="随机生成细胞", command=lambda: life_game.map.randomize_cells(random_density.get()))
    randomize_button.grid(row=4, column=0, pady=5)

    clear_button = tk.Button(button_frame, text="清空细胞", command=life_game.clear)
    clear_button.grid(row=5, column=0, pady=5)

    quit_button = tk.Button(button_frame, text="退出", command=root.quit)
    quit_button.grid(row=6, column=0, pady=5)

    CAnvas.bind("<Button-1>", lambda event: life_game.toggle_cells(event))



if __name__ == '__main__':
    Set_UI()
    root.mainloop()

