#  UTF-8
import os

class Settings:
    """设置模块"""

    def __init__(self):
        """初始化各项设置"""
        #  相关信息获取
        self.os_informatin = os.name

        #  初始化游戏运行所需参数
        # 注：所有文件路径均采用相对路径
        self.game_name = "星玄"
        self.ship = (1600, 900)
        self.image = "Material\\image\\icon1.bmp"  # 背景图片路径（icon和icon1）
        self.word_path = "Material\\word_body\\simkai.ttf"  # 字体文件路径
        self.word_color = (150, 233, 255)  # 字体颜色
        self.fps = 50  # 刷新率
        self.date_root_path = "Data"  # 数据库根目录

        #  从相关管理模块抓取信息
        #  种子管理模块
        self.bt_much = 20  # 注：个数从零开始若为4则实际有5个
        self.bt_information = []


class Value_exchange:
    """获取管理模块的值"""

    def __init__(self):
        pass


class Value_base:
    """向各个模块输出值"""

    def __init__(self):
        # 未经过计算的值（直接赋值的）
        self.values_all_raw = Settings()
        self.game_name = self.values_all_raw.game_name  # 游戏名
        self.ship = self.values_all_raw.ship  # 窗口大小
        self.image = self.values_all_raw.image  # 背景图片路径
        self.word_path = self.values_all_raw.word_path  # 字体文件路径
        self.word_color = self.values_all_raw.word_color  # 字体颜色
        self.fps = self.values_all_raw.fps  # 刷新率
        self.bt_much = self.values_all_raw.bt_much  # 种子数量
        self.bt_information = self.values_all_raw.bt_information  # 种子信息
        self.date_root_path = self.values_all_raw.date_root_path  # 根目录数据库

