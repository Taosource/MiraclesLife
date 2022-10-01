import time

# 自己的
from setting import Settings
import system_time


class Game_Time:
    """管理游戏时间"""

    def __init__(self):
        self.settings = Settings()
        self.game_time_system = system_time.game_time_system()

    def time_exchange(self):
        pass
