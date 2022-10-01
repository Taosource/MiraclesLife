import time

# 自己的
from setting import Settings


class game_time_system:
    """管理系统时间"""

    def __init__(self):
        self.settings = Settings()

    def time_get(self):
        game_time_systems = time.time()
