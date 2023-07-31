# encode = "UTF-8"


import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
# '../'注：表示添加上一级目录。例：'../../'  表示添加上两级目录
# 将项目根目录添加到python环境中,方便调用所有模块


from OfficialModel import SolarSystemRoutine
from Redis import GetDesignateInstance
# 导入自定义模块



# 测试
tt = GetDesignateInstance.GetInstance()
c = tt.get_value({'ID':'2345'})
print(f'修改前{c}')
# print(type(tt.get_value({'ID':'2345'})))
info = {'ID':'2345', 'x':c.x, 'y':c.y}
a = SolarSystemRoutine.PlantRunTime(info)
n = a.run()
print(f'修改后{n}')