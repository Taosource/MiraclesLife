# UTF-8

import os

from setting import Value_base


class Contral_main:
    """中心控制模块"""

    def __init__(self):
        #  导入设置
        self.settings = Value_base()
        self.date_root_path = self.settings.date_root_path

    def data_informations_get(self):
        dirpaths = []
        file_folder = []
        file = []
        root_path = os.getcwd()
        path = os.path.join(root_path, self.date_root_path)
        for dirpath, dirnames, filenames in os.walk(path):
            dirpaths.append(dirpath)
            if len(dirnames) != 0:
                for dirname in dirnames:
                    file_folder.append(os.path.join(dirpath, dirname))
            if len(filenames) != 0:
                for filename in filenames:
                    file.append(os.path.join(dirpath, filename))
        return dirpaths, file_folder, file

    def data_informations_make(self):
        file_information = []  # 该列表包含所有文件信息
        # 0：文件目录（由一个字典储存） 1：文件大小信息
        first_floor = {'Date_run': 'Data_base\\Data\\Data_run',
                       'Date_archive': 'Data_base\\Data\\Data_archive',
                       'Date_model': 'Data_base\\Data\\Data_model',
                       'Date_seed': 'Data_base\\Data\\Data_seed',

                       }  # 第一层目录

        information = Contral_main()
        information = information.data_informations_get()  # 目录及文件信息
        # 以下部分为解析所获取的信息
        root_path = information[0]
        root_path = root_path[0]  # 得到数据库根目录所在位置
        first_floor_info = information[1]  # 获取目录下所有文件夹
    # 数据库目录完整效验
        for name in first_floor:
            # print(name)
            paths = root_path[0:18] + ''
            names = str(paths + first_floor[name])
            print(names)
            if names in first_floor_info:
                print("目录完整")
            else:
                print("目录缺失")

        file_information.append(first_floor)

        print(information)
        print(root_path)
        print(first_floor_info)


a = Contral_main()
a.data_informations_make()
