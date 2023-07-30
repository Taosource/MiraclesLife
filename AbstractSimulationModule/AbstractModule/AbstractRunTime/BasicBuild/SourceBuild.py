# encode = "UTF-8"


"""该模块为整个抽象模拟模块中最底层的运行时基类\n
运行时：本项目中，我们将所有能对数据对象进行操作的函数、类及以上更高层次的代码封装称为运行时。\n
所有运行时的抽象基类称为源运行时（即本模块中的抽象基类），\n
而所有运行时的父类则称为根运行时。\n
真正执行数据操作的称为运行时。\n"""


import abc
# 导入python包


class SourceRunTime(abc.ABC):
    """源运行时,为一个抽象基类，实现了所有必须的接口\n
    所需实现的接口如下：\n
    run_x接口, run_y接口,"""
    
    @abc.abstractmethod
    def run_x(self):
        """x坐标运行的接口"""
        
        pass
    
    
    @abc.abstractmethod
    def run_y(self):
        """y坐标运行的接口"""
        
        pass