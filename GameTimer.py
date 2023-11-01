import tkinter as tk
from tkinter import messagebox
import random
import copy



class GameTimer:
    def __init__(self, LifeGame, interval_ms=2000):
        self.life_game = LifeGame
        self.interval_ms = interval_ms
        self.running = False


    def start(self):
        self.running = True
        self.tick()

    def stop(self):
        self.running = False

    # 修改 GameTimer.py 中的 tick 方法
    def tick(self):
        if self.running:
            changed_cells = self.life_game.update()  # 获取状态发生改变的细胞位置
            self.life_game.map.draw_changed_cells(changed_cells)  # 仅重新绘制状态发生改变的细胞
            self.life_game.root.after(self.interval_ms, self.tick)


