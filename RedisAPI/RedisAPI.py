#  encoding = 'UTF_8'

import redis
# 导入第三方库


# Datas = redis.Redis(host = '127.0.0.1', port = 6379, password = 12345, decode_responses = True, charset = 'UTF-8', encoding = 'UTF-8') 

# Datas.set('test', 'test')


# print(Datas.get('test'))


class ApiAbstractInitialize:
    """数据库连接API，通过该api进行数据管理\n
    该部分以后将会移交EC负责，故现在简化处理"""


    def __init__(self):
        """初始化"""
        self.datas = redis.Redis(host = '127.0.0.1', port = 6379, password = 12345, decode_responses = True, charset = 'UTF-8', encoding = 'UTF-8')
        
    
    def make_name(self):
        """生成键的储存名"""
        return_name = int(self.datas.get('make_name')) + 1
        self.datas.set('make_name', return_name)
        return return_name


    def parse(self, input_datas):
        """解析数据"""
        w_datas = dict(input_datas)
        self.datas.hmset(self.make_name(), w_datas)




# def ApiAbstractInitialize():
#     return Datas

