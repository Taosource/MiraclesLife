# encode = “UTF-8”

from collections import namedtuple
# 导入python第三方库

from RedisAPI import RedisAPI
# 导入自定义包

BASE_CONSTRUCTION_PARAMETERS_PLANET = ['x', 'y']
'''基础构造参数,该参数将决定所有基本数据对象的构成\n
该参数为一个列表，列表内的值将决定基本数据对象的属性\n
参数解释：\n
x-类型：整形，功能：确定地图的x轴\n
x-类型：整形，功能：确定地图的y轴\n
'''


THE_UNDERLYING_DATA_OBJECT_PLANET = namedtuple('THE_UNDERLYING_DATA_OBJECT_PLANET', BASE_CONSTRUCTION_PARAMETERS_PLANET)
#  x, y, types, sequences = x坐标，y坐标，类型，编号，时序编号
'''定义基础数据对象\n
The underlying data object 翻译：基础数据对象'''


class MakeZeorPlanet:
    """进行所有星球基础数据对象初始化"""

    def __init__(self, config = None):
        self.config = dict(config)
    
    def parse(self):
        """解析传入数据"""
    

def MakeX(maths):
    list_x = list(range(10))
    return list_x[maths]


def MakeY(maths):
    list_y = list(range(10))
    return list_y[maths]

def alls():
    allss = []
    for i in range(10):
        allss.append((MakeX(i), MakeY(i)))
    return allss 


datas =[]

def Make():
    global datas
    for i in range(1):
        ss = [THE_UNDERLYING_DATA_OBJECT_PLANET(x, y) for x, y in alls()]
        datas = datas + ss

    

Make()

print(datas[5].x)


if __name__ == '__main__':
    Make()