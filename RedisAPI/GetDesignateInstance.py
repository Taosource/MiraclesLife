# encode = "UTF-8"


import os
import sys
# 导入python第三方库


import RedisAPI
# 导入自定义模块


class GetInstance():
    """获取实例。
    通过对RedisAPI的二次封装实现。
    即：通过调用RedisAPI获取到一组序列化的实例后，反序列化实例。并通过解析实例的信息（ID、types等），
    返回符合条件的一个实例，提供给对应的模块操作"""

    def __init__(self, GetMateInfo:'dict'):
        self.GetMateInfo = dict(GetMateInfo)

    