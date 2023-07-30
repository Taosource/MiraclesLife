# encode = "UTF-8"

"""该模块为太阳系常规模型。
是本游戏中第一个开发的运行时模型，也是最普通的模型。
该模型以太阳系作为简单参照。"""


import os
import sys
# 导入python包


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# '../'注：表示添加上一级目录。例：'../../'  表示添加上两级目录
# 将项目根目录添加到python环境中,方便调用所有模块

from BasicBuild import SourceBuild
# 导入自定义抽象基类
# 导入自定义模块

class test(SourceBuild.SourceRunTime):
    """test"""
    
    def __init__(self):
        self.x = 0
        self.y = 0
        
    def run_x(self):
        print(self.x + 1)
        
    def run_y(self):
        print(self.y + 1)
        
a = test()
a.run_x()
a.run_y()