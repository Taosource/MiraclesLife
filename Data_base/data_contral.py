# UTF-8

import os
from setting import Value_base


class Contral_main:
    """中心控制模块"""

    def __init__(self):
        #  导入设置
        self.settings = Value_base()

    def data_informations(self):
        path_top = "Data_base\\Date"
        print(list(os.walk(path_top)))


a = Contral_main()
a.data_informations()
