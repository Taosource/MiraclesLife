import os

from Data_base.data_contral import Contral_main
from Gui.other_gui import Initiate  # 导入Gui包相关内容


class Run_game:
    """创建启动类"""

    def __init__(self):
        self.root_path = os.getcwd()

    def run_game(self):
        """创建游戏启动界面函数"""
        #  数据管理
        print(self.root_path)
        A = Contral_main(self.root_path)
        A.info_file_into()

        # 游戏初始界面
        initiates = Initiate()
        initiates.initiate_gui()


if __name__ == '__main__':
    game = Run_game()
    game.run_game()
