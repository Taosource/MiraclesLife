# encode = "UTF-8"


import os
import sys
import pickle
# 导入python第三方库


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
# '../'注：表示添加上一级目录。例：'../../'  表示添加上两级目录
# 将项目根目录添加到python环境中,方便调用所有模块

import Redis.RedisAPI
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
        self.redis_api = Redis.RedisAPI.ApiAbstractInitialize()
        # 使用RedisAPI下的ApiAbstractInitialize类

    # @classmethod
    def computes(self, ID:'int'):
        """通过ID计算出该实例储存的位置"""
        ID = int(ID)
        IDs = ID
        # main_key_name = ''
        # key_name = ''
        main_counts = 0
        counts = 0
        while ID // 100 > 0:
            main_counts += 1
            IDs -= 100
            if IDs < 100:
                break

        s = main_counts * 100
        id_key = ID - s
        while (ID - s) // 10 > 0:
            counts += 1
            id_key -= 10
            if id_key < 10:
                break

        return str(main_counts), str(counts)

    def get_value(self, GetMateInfo:'dict'):
        """获取值"""
        info = dict(GetMateInfo)
        # print(info)
        main_key_name, key_name = GetInstance.computes(self, info['ID'])
        dd = self.redis_api.read_datas(main_key_name, key_name)
        dd = pickle.loads(dd[0])
        # print(dd)
        # print(dd[int(info['ID'])[-1]])
        # print(dd[int(str(info['ID'])[-1])])
        return dd[int(str(info['ID'])[-1])]
    
    
    def set_value(self,SetMateInfo:'dict'):
        """修改值"""
        info = dict(SetMateInfo)
        main_key_name, key_name = GetInstance.computes(self, info['ID'])
        last_value = self.redis_api.read_datas(main_key_name, key_name)
        change_value = last_value[int(str(info['ID'])[-1])]
        change_value.x, change_value.y = info['x'], info['y']
        last_value[int(str(info['ID'])[-1])] = change_value
        datas = last_value
        value = pickle.dumps(datas)
        self.redis_api.set_datas(main_key_name = main_key_name,
                                 keys = key_name,
                                 value = value)

    

a = GetInstance()
print(a.get_value({'ID':'2345'}))