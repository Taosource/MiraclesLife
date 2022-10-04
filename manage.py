from Gui.other_gui import Initiate  # 导入Gui包相关内容
from setting import Settings


class Open_Gui:
    """创建启动类"""

    def __init__(self):
        self.settings = Settings()  # 导入设置的相关参数

    def game_gui8(self):
        """创建游戏启动界面函数"""
        initiates = Initiate()
        initiates.initiate_gui()


if __name__ == '__main__':
    game1 = Open_Gui()
    game1.game_gui8()

# (True, [0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 9, 2, 9, 2, 1])
