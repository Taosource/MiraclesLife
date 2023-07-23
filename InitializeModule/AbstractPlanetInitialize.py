# encode = “UTF-8”

from collections import namedtuple
import sys
import os
import pickle
import time
# 导入python第三方库

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# '../'注：表示添加上一级目录。例：'../../'  表示添加上两级目录
# 将项目根目录添加到python环境中,方便调用所有模块



from RedisAPI import RedisAPI
# 导入自定义包

BASE_CONSTRUCTION_PARAMETERS_PLANET = ['ID','x', 'y']
"""基础构造参数,该参数将决定所有基本数据对象的构成\n
该参数为一个列表，列表内的值将决定基本数据对象的属性\n
参数解释：\n
x-类型：整形，功能：确定地图的x轴\n
x-类型：整形，功能：确定地图的y轴\n
"""


THE_UNDERLYING_DATA_OBJECT_PLANET = namedtuple('THE_UNDERLYING_DATA_OBJECT_PLANET', BASE_CONSTRUCTION_PARAMETERS_PLANET)
#  x, y, types, sequences = x坐标，y坐标，类型，编号，时序编号
"""定义基础数据对象\n
The underlying data object 翻译：基础数据对象"""


ID_COUNTER = 0
# ID计数器
AXIS_COUNTER = 0
# 坐标计数器


class MakeZeorPlanet:
    """进行所有星球基础数据对象初始化"""

    def __init__(self, config = None):
        self.config = dict(config)
    
    def parse(self):
        """解析传入数据"""
        pass
    

def MakeX(maths:'int') -> int:
    """生成X坐标"""
    # list_x = list(range(10))
    return maths


def MakeY(maths:'int') -> int:
    # list_y = list(range(10))
    return maths


def MakeID() -> str:
    """生成ID"""
    global ID_COUNTER
    # alphabet = [chr(x) for x in range(65, 91)]
    # 创建一个A-Z的英文字母列表
    # return alphabet[maths - int(maths//10)] + maths//
    return_ID = ID_COUNTER
    ID_COUNTER += 1
    # print(ID_COUNTER)
    # print(return_ID)
    return str(return_ID)
    

def alls():
    allss = []
    for i in range(10):
        ID = MakeID()
        allss.append((ID, MakeX(int(ID)), MakeY(int(ID))))
    # print(allss)
    return allss 
    



def Make(mate_data:'dict') -> None:
    write_data = RedisAPI.ApiAbstractInitialize()
    for i in range(int(mate_data['planet_size'][0:-1])):

        ss = [THE_UNDERLYING_DATA_OBJECT_PLANET(ID, x, y) for ID, x, y in alls()]
        datas = pickle.dumps(ss)
        write_data.write_datas({str(i)[-1]: datas})
        
    # print(pickle.loads(write_data.read_datas(main_key_name = str(1), keys = str(0))[0]))
    # print(pickle.loads(write_data.read_datas(main_key_name = str(9), keys = str(9))[0]))



if __name__ == '__main__':
    t = time.time()
    Make()
    t1 = time.time()
    # # print(f'测试完毕，本次测试共100000000（1亿实例）\n共消耗时间为{t1 - t}s')
    # write_data = RedisAPI.ApiAbstractInitialize()
    # print(pickle.loads(write_data.read_datas(main_key_name = str(1), keys = str(0))[0]))
    # print(pickle.loads(write_data.read_datas(main_key_name = str(9), keys = str(9))[0]))
    # # mer = write_data.read_datas(main_key_name = 'used_memory_human')
    # mer = write_data.redis_info()['used_memory_human']
    # print(f'测试完毕，本次测试共100000000（1亿实例）\n共消耗时间为{t1 - t}s')
    # vers = write_data.redis_info()['redis_version']
    # oss = write_data.redis_info()['os']
    # mers = write_data.redis_info()['used_memory_peak_human']
    # # print(write_data.redis_info())
    # print(f'当前内存使用量为{mer}\n数据库版本为{vers}\n操作系统为{oss}\n内存占用峰值为{mers}')