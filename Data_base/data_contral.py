# UTF-8

import csv
import os

from setting import Value_base


class Contral_main:
    """中心控制模块"""

    def __init__(self, root_path):
        #  导入设置，从设置中获取相关参数
        self.data_dump_path = root_path + "\\Data_base\\Data_dump.csv"
        self.settings = Value_base()
        self.date_root_path = self.settings.date_root_path

        # 从相关模块获取参数
        self.root_path = root_path

        # 专属参数
        self.file_information = []  # 该列表包含所有文件信息

    def data_informations_get(self):
        print(self.root_path)
        dirpaths = []
        file_folder = []
        file = []

        root_path = self.root_path
        root_path = root_path + "\\Data_base"
        path = os.path.join(root_path, self.date_root_path)  # 获取绝对路径

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
        file_information = []
        information = Contral_main.data_informations_get(self)  # 调用data_informations_get函数获取所有目录及文件信息
        # 0：文件目录（由一个字典储存） 1：文件大小信息及文件归属（ascription）
        first_floor = {'Data_run': 'Data_base\\Data\\Data_run',
                       'Data_archive': 'Data_base\\Data\\Data_archive',
                       'Data_model': 'Data_base\\Data\\Data_model',
                       'Data_seed': 'Data_base\\Data\\Data_seed',

                       }  # 第一层目录
        file_information.append(first_floor)

        # 以下部分为解析所获取的信息
        print(information)
        root_path = information[0]
        root_path_len = len(str(root_path[0]))
        print(root_path)
        root_path = root_path[0]  # 得到数据库根目录所在位置
        first_floor_info = information[1]  # 获取目录下所有文件夹
        # 数据库目录完整效验
        intact = []  # 0为缺失，1为为完整
        for name in first_floor:
            # print(name)
            paths = root_path[0:18]
            names = str(paths + first_floor[name])
            print(names)
            if names in first_floor_info:
                intact.append(1)
                print("目录完整")
            else:
                intact.append(0)
                print("目录缺失")

        # file_echange_one = information[0]  # 包含总数据库Data
        file_echange_two = information[1]  # 总数据库Data下面的所有文件夹
        file_echange_three = information[2]  # 总数据库Data下面的所有文件夹下的所有非文件夹文件

        #  以下4行创建储存各个数据模块所包含的文件
        data_archive = []
        data_model = []
        data_run = []
        data_seed = []

        for two in file_echange_two:  # 逐个遍历总数据库Data下面的所有文件夹
            for three in file_echange_three:  # 逐个遍历总数据库Data下面的所有文件夹下的所有非文件夹文件
                threes = three[0:-13]  # 注意所有数据文件名称为长为8，格式为csv （此处为获取每个文件前面的路径部分以便确定文件所属文件夹）
                twos = two[root_path_len + 1:-1] + two[-1]  # 得到总数据库Data下每一个文件夹的名称
                if two == threes:  # 通过确定文件前面的路径相同来判断该文件命名否合程序要求
                    #  以下的if语句为判断文件归属并将文件名加入到对应列表中
                    if twos == 'Data_archive':
                        data_archive.append(three[-12:])
                        size = os.stat(three)
                        data_archive.append(size.st_size)  # 将该文件大小添加到列表中文件名元素后面 注意单位为字节
                    if twos == 'Data_model':
                        data_model.append(three[-12:])
                        size = os.stat(three)
                        data_model.append(size.st_size)
                    if twos == 'Data_run':
                        data_run.append(three[-12:])
                        size = os.stat(three)
                        data_run.append(size.st_size)
                    if twos == 'Data_seed':
                        data_seed.append(three[-12:])
                        size = os.stat(three)
                        data_seed.append(size.st_size)

        info = [data_archive, data_model, data_run, data_seed]
        file_information.append(info)  # 将文件名称存入改列表（位于第二个元素），总共四个列表代表四个文件夹依次对应
        info_w_one = Data_writer(file_information)
        info_w_one.data_informations_write()
        info_w_two = Data_writer(info)
        info_w_two.data_informations_write()

        return file_information  # , information, root_path, first_floor_info,

    def info_file_into(self):
        """文件详细信息获取"""

        # def seed_info():
        """种子信息处理"""
        seed_info = {}  # 储存种子信息（key为种子名（为字符串）value为一个列表）
        # 列表中第一个元素为种子编号，第二个为种子绝对路径，第三个为大小
        seed_number = []
        root_path = self.root_path  # 得到根目录
        root_path = root_path + "\\Data_base"  # 得到数据库根目录
        path = os.path.join(root_path, self.date_root_path)  # 将数据库根目录与数据目录组合得到绝对路径
        info_path = Contral_main.data_informations_make(self)  # 获取文件路径名称等信息
        info_paths = info_path[0]
        # info_file = info_path[1]
        info_paths = list(info_paths)
        for info_path in info_paths:
            if info_path == "Data_seed":
                make_path = path + "\\Data_seed"
                for dirpath, dirnames, filenames in os.walk(make_path):
                    seed_number.append(len(filenames))
                    seed_info = dict.fromkeys(range(len(filenames)))
                    b = 0
                    for i in filenames:
                        r_path = dirpath + "\\" + i

                        with open(r_path, "r", encoding="UTF-8", newline='') as f:
                            read = csv.reader(f)
                            next(read)
                            a = 0
                            for info in read:
                                # info = str(info)
                                if a == 0:
                                    seed_info[b] = dict.fromkeys(range(3))  # seed_info={path:{}{}{}, }
                                    A = seed_info[b]
                                    A[0] = info[1]
                                if a == 1:
                                    A[1] = info[1]
                                if a == 2:
                                    A[2] = info[1]

                                a += 1
                        b += 1
        seed_info = seed_info
        info_w_three = Data_writer(seed_info, 1)
        info_w_three.data_informations_write()


class Data_writer:
    """负责数据写入"""

    def __init__(self, info_write, write_code=None):
        # 初始化需要写入的值
        self.info_write = info_write

        # 特殊参数（1：对应字典写入模式（默认为字符串写入可以为空））
        self.write_code = write_code

        # 从其他模块导入必要值
        self.root_path = os.getcwd()
        self.value = Contral_main(self.root_path)
        self.data_dump_path = self.value.data_dump_path

    def data_informations_write(self):
        # file_information = Contral_main.data_informations_make(self)  # 调用data_informations_make函数获取处理好的目录及文件信息
        if self.write_code == 1:
            with open(self.data_dump_path, "a+", encoding="UTF-8", newline='') as info:
                writer = csv.writer(info)
                for key, value in self.info_write.items():
                    writer.writerow([key, value])
        else:
            with open(self.data_dump_path, "a+", encoding="UTF-8", newline='') as infos:
                file_write = csv.writer(infos)
                file_write.writerows(self.info_write)
