import unittest
from unittest.mock import patch, Mock
from GameTimer import GameTimer

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
