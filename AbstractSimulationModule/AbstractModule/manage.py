# encode = "UTF-8"

import sys
import os
# 导入python第三方包


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
# 添加上两级目录
# 将项目根目录添加到python环境中,方便调用所有模块

# print(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from InitializeModule import manage
# 导入自定义包


mate_data = {'run_type': 'Abstract', 'planet_size': '10000', 'map_size': '1000000'}
""" run_type:决定了初始化模块的初始化方式\n
    planet_size:初始化时的星球数量\n
    map_size:地图的大小(建议大小为星球数量的100倍)\n
    """


manage.manages(mate_data)


class AbstractMange():
    """抽象模拟模块的总控制类\n
    负责控制所有抽象模拟的行为"""