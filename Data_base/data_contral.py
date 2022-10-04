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
        return dirpath, file_folder, file


files = Contral_main()
print(files.data_informations_get())
