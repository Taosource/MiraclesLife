# python3.8.10
# UTF-8

# 导入第三方包
import os

# 导入自己的包
from Data_base.data_contral import Contral_main
from Gui.game_gui import Gui
from Gui.other_gui import Initiate  # 导入Gui包相关内容


class Run_game:
    """创建启动类"""

    def __init__(self):
        self.root_path = os.getcwd()

    def run_game(self):
        """创建游戏启动界面函数"""
        #  数据管理
        # print(self.root_path)
        A = Contral_main(self.root_path)
        A.info_file_into()

        # 游戏初始界面
        initiates = Initiate()
        initiates.initiate_gui()

        # 游戏主界面
        Gui_main = Gui()
        Gui_main.game_gui()


if __name__ == '__main__':
    game = Run_game()
    game.run_game()
