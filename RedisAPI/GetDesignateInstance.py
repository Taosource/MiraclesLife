# encode = "UTF-8"


import os
import sys
import pickle
# 导入python第三方库


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# '../'注：表示添加上一级目录。例：'../../'  表示添加上两级目录
# 将项目根目录添加到python环境中,方便调用所有模块

import RedisAPI
# 导入自定义模块


class GetInstance():
    """获取实例。
    通过对RedisAPI的二次封装实现。
    即：通过调用RedisAPI获取到一组序列化的实例后，反序列化实例。并通过解析实例的信息（ID、types等），
    返回符合条件的一个实例，提供给对应的模块操作"""

    def __init__(self):
        """初始化"""
        # self.GetMateInfo = dict(GetMateInfo)
        # 实践鸭子类思想，无论传入任何类型的值都转化为字典
        self.redis_api = RedisAPI.ApiAbstractInitialize()
        # 使用RedisAPI下的ApiAbstractInitialize类

    # @classmethod
    def computes(self, ID:'int'):
        """通过ID计算出该实例储存的位置"""
        ID = int(ID)
        # main_key_name = ''
        # key_name = ''
        main_counts = 0
        counts = 0
        while ID // 100 > 0:
            main_counts += 1
            if ID - 100 < 100:
                break

        s = main_counts * 100
        while (ID - s) // 10 > 0:
            counts += 1
            if (ID - s) < 10:
                break

        return str(main_counts), str(counts)

    def get_value(self, GetMateInfo:'dict'):
        info = dict(GetMateInfo)
        print(info)
        main_key_name, key_name = GetInstance.computes(self, info['ID'])
        dd = self.redis_api.read_datas(main_key_name, key_name)
        dd = pickle.loads(dd[0])
        print(dd)

    

a = GetInstance()
a.get_value({'ID':'100'})