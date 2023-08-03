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


class PlantRunTime(SourceBuild.PlantSourceRunTime):
    """星球运行时\n
    继承自星球源运行时，由于为第一个模型，所以并没有其他父类。\n
    在其他模型中可能会存在父类。\n
    该类将实现星球的简单运行。"""
    
    
    def __init__(self, DataMolds:'dict'):
        self.DataMolds = dict(DataMolds)
        
        
    def run_x(self, x):
        return x + 1
    
    
    def run_y(self, y):
        return y + 1
    
    
    def run(self):
        # self.DataMolds.x, self.DataMolds.y = PlantRunTime.run_x(self.DataMolds.x), PlantRunTime.run_y(self.DataMolds.y)        
        # print(self.DataMolds)
        x, y = PlantRunTime.run_x(self, self.DataMolds['x']),PlantRunTime.run_y(self, self.DataMolds['y']) 
        return_value = {'x':x,
                        'y':y}
        return return_value

