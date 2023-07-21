# encode = "UTF-8"

import sys
import os
# 导入python第三方库

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# '../'注：表示添加上一级目录。例：'../../'  表示添加上两级目录
# 将项目根目录添加到python环境中,方便调用所有模块

import InitializeModule.AbstractPlanetInitialize



def manages(mate_data:'dict') -> object:
    if mate_data['run_type'] == 'Abstract':
        i = InitializeModule.AbstractPlanetInitialize.Make(mate_data)
        # i.Make(mate_data)
    else: 
        pass

