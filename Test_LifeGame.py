import unittest
from unittest.mock import mock_open, patch, Mock
import tkinter as tk
from tkinter import Canvas, Tk
from LifeGame import LifeGame

class TestLifeGame(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=300, height=300)
        self.game = LifeGame(10, 10, 30, self.root, self.canvas)
        self.map = self.game.map
    def tearDown(self):
        self.root.destroy()

    def test_update(self):
        # 设置初始地图状态
        initial_state = [
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        # 设置地图状态为初始状态
        self.game.map.grid = initial_state
        self.game.stable = True
        # 调用 update 方法来更新地图状态
        #self.game.update()
        # 验证更新后的地图状态是否与预期一致
        expected_state = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(self.game.map.grid, expected_state)

    def test_is_stable(self):
        # 设置初始地图状态
        initial_state1 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.game.map.grid = initial_state1
        self.game.stable = True
        expected_state1 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        with patch.object(self.game, 'check_stable') as mock_check_stable, patch.object(self.game,
                                                                                        'show_stable_message'):
            # 调用 update 方法来更新地图状态
            self.game.update()
            # 验证 check_stable 方法是否被调用
            mock_check_stable.assert_called_once()
            # 验证游戏的 stable 状态
            self.assertTrue(self.game.stable)

    def test_count_alive_neighbors(self):
        # 设置地图状态
        self.game.map.grid = [
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

        # 验证细胞 (2, 2) 的邻居数量
        neighbors_1 = self.game.count_alive_neighbors(2, 2)
        self.assertEqual(neighbors_1, 4)

        # 验证细胞 (0, 0) 的邻居数量
        neighbors_2 = self.game.count_alive_neighbors(0, 0)
        self.assertEqual(neighbors_2, 1)

        # 验证细胞 (4, 4) 的邻居数量
        neighbors_3 = self.game.count_alive_neighbors(4, 4)
        self.assertEqual(neighbors_3, 2)


    def test_show_stable_message(self):
        # 模拟稳定状态
        stable_state = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        for _ in range(self.game.MAX_REPEATED_STATES):
            self.game.check_stable(tuple(map(tuple, stable_state)))
        # 使用 patch 模拟 messagebox.showinfo 方法
        with patch('tkinter.messagebox.showinfo') as mock_showinfo:
            self.game.show_stable_message()
            # 验证 messagebox.showinfo 方法是否被调用，以及传递给它的参数
            mock_showinfo.assert_called_once_with("Message", "细胞状态已稳定。")


    def test_clear(self):
        # 设置地图状态为非空状态
        initial_state = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        self.game.map.grid = initial_state

        # 调用 clear 方法
        self.game.clear()

        # 验证地图状态是否已清空
        expected_state = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(self.game.map.grid, expected_state)

    def test_toggle_cells(self):
        # 模拟点击事件，将特定细胞的状态进行切换
        click_event = Mock()
        click_event.x = 2 * self.game.cell_size
        click_event.y = 3 * self.game.cell_size

        # 初始化特定细胞为死亡状态 (0)
        self.game.map.grid[3][2] = 0

        # 调用 toggle_cells 方法模拟点击事件
        self.game.toggle_cells(click_event)

        # 验证特定细胞状态是否已切换为存活状态 (1)
        self.assertEqual(self.game.map.grid[3][2], 1)

if __name__ == '__main__':
    unittest.main()
