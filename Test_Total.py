import unittest
from unittest.mock import mock_open, patch, Mock

from tkinter import Canvas, Tk
from GameMap import GameMap
from LifeGame import LifeGame
from GameTimer import GameTimer

class TestGameMap(unittest.TestCase):
    def setUp(self):
        self.width = 10
        self.height = 10
        self.cell_size = 20
        self.canvas = Canvas(None)  # 创建一个Canvas对象，或者使用mock
        self.game_map = GameMap(self.width, self.height, self.cell_size, self.canvas)

    def create_mock_event(self, x, y):
        # 创建一个模拟鼠标事件的辅助方法
        class MockEvent:
            def __init__(self, x, y):
                self.x = x
                self.y = y
        return MockEvent(x, y)

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
        self.game.update()
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
            [0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 1, 1, 1],
            [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 1, 1, 1],
            [0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
            [0, 1, 0, 0, 0, 1, 1, 1, 1, 1]
        ]
        neighbors_1 = self.game.count_alive_neighbors(0, 1)
        self.assertEqual(neighbors_1, 1)
        neighbors_2 = self.game.count_alive_neighbors(0, 0)
        self.assertEqual(neighbors_2, 0)
        neighbors_3 = self.game.count_alive_neighbors(1, 1)
        self.assertEqual(neighbors_3, 2)
        neighbors_4 = self.game.count_alive_neighbors(1, 3)
        self.assertEqual(neighbors_4, 3)
        neighbors_5 = self.game.count_alive_neighbors(3, 2)
        self.assertEqual(neighbors_5, 4)
        neighbors_6 = self.game.count_alive_neighbors(3, 4)
        self.assertEqual(neighbors_6, 5)
        neighbors_7 = self.game.count_alive_neighbors(6, 8)
        self.assertEqual(neighbors_7, 6)
        neighbors_8 = self.game.count_alive_neighbors(8, 1)
        self.assertEqual(neighbors_8, 7)
        neighbors_9 = self.game.count_alive_neighbors(8, 8)
        self.assertEqual(neighbors_9, 8)


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

class TestGameTimer(unittest.TestCase):
    def setUp(self):
        # 创建一个模拟的 LifeGame 实例
        self.life_game = Mock()
        # 创建一个 GameTimer 实例并传递模拟的 LifeGame 实例
        self.timer = GameTimer(self.life_game)

    def test_start(self):
        # 测试 start 方法是否正确设置了 running 标志为 True
        self.timer.start()
        self.assertTrue(self.timer.running)

    def test_stop(self):
        # 测试 stop 方法是否正确设置了 running 标志为 False
        self.timer.running = True  # 模拟已经启动的定时器
        self.timer.stop()
        self.assertFalse(self.timer.running)

    @patch('GameTimer.GameTimer.tick')
    def test_tick(self, mock_tick):
        # 测试 tick 方法是否正确调用了 tick
        self.timer.running = True  # 模拟已经启动的定时器
        self.timer.tick()
        mock_tick.assert_called_once()

if __name__ == '__main__':
    unittest.main()
