# encode = "UTF-8"

from Redis import RedisAPI


# 导入数据库操作API
# 导入自定义模块

class SetInstance:
    """写入实例。
    对RedisAPI的二次封装。
    通过RedisAPI实现了修改后数据的写入。"""

    def __init__(self):
        """初始化"""
        self.redis_api = RedisAPI.ApiAbstractInitialize()
        # 实例化一个数据api，通过调用该实例的不同方法实现数据操作

    def set_value(self, SetMateInfo: 'dict'):
        """写入修改后的值"""
        info = dict(SetMateInfo)
        # 防止错误，再次将传入值转化为字典
        self.redis_api.set_datas(info['main_key_name'], info['set_value'])
