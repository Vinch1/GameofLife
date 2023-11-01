import unittest
from tkinter import Canvas  # 请根据你的实际情况导入Canvas类
from unittest.mock import mock_open, patch, Mock

from GameMap import GameMap

class TestGameMap(unittest.TestCase):
    def setUp(self):
        self.width = 10
        self.height = 10
        self.cell_size = 20
        self.canvas = Canvas(None)  # 创建一个Canvas对象，或者使用mock
        self.game_map = GameMap(self.width, self.height, self.cell_size, self.canvas)

    def test_toggle_cell(self):
        # 测试toggle_cell方法是否正确地切换细胞状态
        initial_state = self.game_map.grid[0][0]
        self.game_map.toggle_cell(self.create_mock_event(0, 0))
        self.assertNotEqual(initial_state, self.game_map.grid[0][0])

    def test_clear_cells(self):
        # 测试clear_cells方法是否将所有细胞状态清零
        self.game_map.grid[0][0] = 1
        self.game_map.clear_cells()
        self.assertEqual(self.game_map.grid, [[0] * self.width for _ in range(self.height)])

    def create_mock_event(self, x, y):
        # 创建一个模拟鼠标事件的辅助方法
        class MockEvent:
            def __init__(self, x, y):
                self.x = x
                self.y = y
        return MockEvent(x, y)

    @patch('random.random', Mock(side_effect=[0.1, 1, 0.1, 1, 0.1, 1, 0.1, 1, 0.1]))
    def test_randomize_cells(self):
        self.map = GameMap(3, 3, 30,self.canvas)

        self.map.randomize_cells(0.5)
        cnt = 0
        for i in range(self.map.height):
            for j in range(self.map.width):
                if self.map.grid[i][j] == 1:
                    cnt += 1
        print(cnt)
        self.assertEqual(5, cnt)

if __name__ == '__main__':
    unittest.main()
