#  UTF-8
import os
import re

class Settings:
    """设置模块"""

    def __init__(self):
        """初始化各项设置"""
        #  从系统获取相关信息
        self.os_informatin = os.name  # 获取系统类型
        self.root_path = os.getcwd()  # 获取游戏运行时的根目录（注：该目录与settings运行时所处的目录有关
        # 所以settings文件的位置至关重要该根目录参数将会在多个位置使用 ）

        #  初始化游戏运行所需参数
        # 注：所有文件路径均采用相对路径
        self.game_name = "涌现：控制台"
        self.ship = (1600, 900)
        self.game_gui = os.getcwd() + "\\Material\\image\\gui1.bmp"  # 游戏gui
        self.image = "Material\\image\\icon1.bmp"  # 背景图片路径（icon和icon1）
        self.word_path = "Material\\word_body\\simkai.ttf"  # 字体文件路径
        self.word_color = (150, 233, 255)  # 字体颜色
        self.fps = 50  # 刷新率
        self.date_root_path = "Data"  # 数据库根目录
        self.operate_path = "\\OperationalData\\Serialnumber.csv"  # 事件触发限制文件

        #  从相关管理模块抓取信息
        #  种子管理模块
        self.bt_much = 20  # 注：个数从零开始若为4则实际有5个
        self.bt_information = []


class Value_exchange:
    """获取管理模块的值并处理"""

    def __init__(self):
        self.data_dump = os.getcwd() + "\\Data_base\\Data_dump.csv"

    def value_get(self):
        """从数据转存文件获取值"""
        data = []
        with open(self.data_dump, "r", encoding="UTF-8", newline='') as f:
            for line in f:
                line = line.rstrip('\r')
                line = line.rstrip('\n')
                line = line.rstrip('\r')
                # line = line.rstrip('\\\\')
                data.append(line)  # 将文件逐行读取，将每一行作为一个元素添加到列表中
        pi_pei = data[5]
        # line = "this hdr-biz model args= server"

        patt = r'csv'
        pattern = re.compile(patt)
        result = pattern.findall(pi_pei)
        bt_number = len(result) - 1
        # 以上四行是通过判断csv文件的数量来确定种子数量（字符串匹配）

        data.insert(0, bt_number)  # 将种子数量添加带列表头
        m_data = data[7:7 + bt_number + 1]
        seed_info = []
        str_pat = re.compile(r'"(.*?)"')  # 匹配字符串，将双引号内的字典单独拿出来
        for i in m_data:
            i = str_pat.findall(i)
            i = eval(i[0])  # 将得到的字符串转化为字典
            seed_info.append(i)
        return data, seed_info

    def values_make(self):
        """处理得到的值"""
        data = Value_exchange.value_get(self)[0]
        seed_info = Value_exchange.value_get(self)[1]
        return data, seed_info
        # print(data)


class Value_base:
    """向各个模块输出值"""

    def __init__(self):
        # 未经过计算的值（直接赋值的）
        self.values_all_raw = Settings()  # 导入设置
        self.game_name = self.values_all_raw.game_name  # 游戏名
        self.ship = self.values_all_raw.ship  # 窗口大小
        self.image = self.values_all_raw.image  # 背景图片路径
        self.game_gui = self.values_all_raw.game_gui  # 游戏UI路径
        self.word_path = self.values_all_raw.word_path  # 字体文件路径
        self.word_color = self.values_all_raw.word_color  # 字体颜色
        self.fps = self.values_all_raw.fps  # 刷新率
        # self.bt_much = self.values_all_raw.bt_much  # 种子数量
        # self.bt_information = self.values_all_raw.bt_information  # 种子信息
        self.date_root_path = self.values_all_raw.date_root_path  # 根目录数据库
        self.root_path = self.values_all_raw.root_path  # 游戏运行根目录
        self.operate_path = self.values_all_raw.operate_path  # 事件触发限制文件目录

        # 经过计算的值
        self.values_make = Value_exchange()
        self.values_make_one = self.values_make.values_make()[0]
        self.values_make_two = self.values_make.values_make()[1]
        self.bt_much = self.values_make_one[0]  # 种子数量
        self.seed_info = self.values_make_two  # 种子信息
