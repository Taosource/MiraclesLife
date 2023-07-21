#  encoding = 'UTF-8'

import redis
# 导入第三方库


# Datas = redis.Redis(host = '127.0.0.1', port = 6379, password = 12345, decode_responses = True, charset = 'UTF-8', encoding = 'UTF-8') 

# Datas.set('test', 'test')


# print(Datas.get('test'))

NAME_COUNTER = 0




class ApiAbstractInitialize:
    """数据库连接API，通过该api进行数据管理\n
    该部分以后将会移交EC负责，故现在简化处理"""


    def __init__(self):
        """初始化"""
        self.datas = redis.Redis(host = '127.0.0.1', port = 6379, password = 12345, decode_responses = False, charset = 'UTF-8', encoding = 'UTF-8')
        # decode_responses只有设置为False才能保证对象能够正确存储，后两个参数为编码
        self.datas.set('make_name', 0)
        # 写入一个名为make_name的键值对，值为0
    
    def make_name(self):
        """生成键的储存名"""
        global NAME_COUNTER
        # return_name = int(self.datas.get('make_name'))
        return_name = int(self.datas.get('make_name'))//100
        self.datas.set('make_name', int(self.datas.get('make_name')) + 1)
        return return_name


    def write_datas(self, input_datas):
        """解析数据"""
        w_datas = dict(input_datas)
        self.datas.hmset(self.make_name(), w_datas)


    def read_datas(self, main_key_name, keys = None):
        """读取数据"""
        if keys is None:
            return self.datas.get(main_key_name)
        else:
            return self.datas.hmget(main_key_name, keys)
        
    def redis_info(self):
        """读取数据库信息"""
        return self.datas.info()




# def ApiAbstractInitialize():
#     return Datas

