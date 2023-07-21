# encode = "UTF-8"

import sys
import os
# 导入python第三方包


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
# 添加上两级目录
# 将项目根目录添加到python环境中,方便调用所有模块

# print(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from InitializeModule import manage
# 导入自定义包


mate_data = {'run_type': 'Abstract', 'planet_size': '10000'}
manage.manages(mate_data)