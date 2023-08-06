# encode = "UTF-8"
"""AbstractRunTime(抽象运行时)管理"""

import os
import sys

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
# '../'注：表示添加上一级目录。例：'../../'  表示添加上两级目录
# 将项目根目录添加到python环境中,方便调用所有模块


# from OfficialModel import SolarSystemRoutine
from AbstractSimulationModule.AbstractModule.AbstractRunTime.OfficialModel import SolarSystemRoutine
from Redis import GetDesignateInstance
from Redis import SetDesignateInstance

# 导入自定义模块


class AbstractRunTimeManage:
    """抽象运行时管理\n
    实现对所有抽象运行时的管理，\n
    1.检测模型（运行时）的增减\n
    2.在正确时刻启动对应的模型（运行时），运行状态管理\n
    3.模型（运行时）的多线程，多进程管理\n"""
    
    
    def __init__(self) -> None:
        self.get_instance = GetDesignateInstance.GetInstance()
        # 初始化一个获取数据的实例
        self.set_instance = SetDesignateInstance.SetInstance()
        # 初始化一个写入数据的实例
        self.run_time = SolarSystemRoutine.PlantRunTime()
        # 初始化一个SolarSystemRoutine模型的运行时实例
        
    def run_manage(self):
        """核心部分，运行模块"""
        
        old_value = self.get_instance.get_value({'ID':'2345'})
        old_value_all = self.get_instance.get_value({'ID':'2345'}, hm = True)
        #  获取需要修改的值
        new_value = self.run_time.run({'x':old_value.x, 'y':old_value.y})
        self.set_instance.set_value()

# # 测试
# tt = GetDesignateInstance.GetInstance()
# c = tt.get_value({'ID':'2345'})
# print(f'修改前{c}')

# # print(type(tt.get_value({'ID':'2345'})))
# info = {'ID':'2345', 'x':c.x, 'y':c.y}
# a = SolarSystemRoutine.PlantRunTime(info)
# n = a.run()
# print(f'修改后{n}')