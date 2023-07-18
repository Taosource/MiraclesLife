#  encoding = 'UTF_8'

import redis


Datas = redis.Redis(host = '127.0.0.1', port = 6379, password = 12345, decode_responses = True, charset = 'UTF-8', encoding = 'UTF-8') 

Datas.set('test', 'test')


print(Datas.get('test'))


class ApiAbstractInitialize:
    """数据库连接API，通过该api进行数据管理"""


    def __init__(self):
        self.datas = redis.Redis(host = '127.0.0.1', port = 6379, password = 12345, decode_responses = True, charset = 'UTF-8', encoding = 'UTF-8')

    
    def parse(self, input_datas):
        pass




# def ApiAbstractInitialize():
#     return Datas

