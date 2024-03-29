# 导入外部第三方库
import os
import time

# 导入第三方包
import pygame
from pygame import VIDEORESIZE
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP

# 导入自己的包
from setting import Value_base

shun_list = []
shun_lists = [0, 1, 2, 3, 4, 5]


def shun_xu(number):
    shun_list.append(number)
    if len(shun_list) == 0 or len(shun_list) >= 6:
        del shun_list[-1]
        return False
    elif number == shun_lists[len(shun_list)]:
        return True, shun_list
    else:
        del shun_list[-1]
        return False


class FileOperations:
    """负责本模块内的所有文件操作"""

    @staticmethod  # 定义静态方法
    def purge_file(root_path, operate_path):  # 接受两个参数，分别为根目录和操作目录（基于根目录）
        """该方法用来执行操作0（清空文件内容）"""
        path = root_path + operate_path  # 组合形成完整的根目录
        path = os.path.join(path)
        with open(path, "w", encoding="UTF-8") as f:  # 以只读模式打开文件指针位于文件开头,原内容将会被删除
            f.truncate()  # 截断函数，用于清空文件内容

    @staticmethod  # 定义静态方法
    def write_file(root_path, operate_path, datas):  # 接受三个参数，分别为根目录和操作目录（基于根目录）和用于写入的数据
        """该方法用来执行操作1（写入内容）"""
        path = root_path + operate_path  # 合成根目录
        path = os.path.join(path)   # 格式化根目录
        with open(path, "a", encoding="UTF-8") as f:
            f.write(datas)

    @staticmethod  # 定义静态方法
    def read_file(root_path, operate_path):  # 接受两个参数，分别为根目录和操作目录（基于根目录）
        """该方法用来执行操作2（读取内容）"""
        path = root_path + operate_path
        path = os.path.join(path)
        reaturn_data = []   # 创建空列表，接受读取出来的内容
        with open(path, "r", encoding="UTF-8") as f:   # 以r模式打开文件
            reaturn_data = f.readlins()  # 将整个文件读取到一个列表中，每一行为列表中的一个元素
            
        return reaturn_data

    def __init__(self, operationcode, operatepath, content=None):
        # 从设置中导入相关初始化参数
        self.settings = Value_base()
        self.root_path = self.settings.root_path

        # 内部的初始化参数
        self.operationcode = operationcode  # 接受操作代码
        self.content = content  # 接受读写内容,可以为空
        self.operatepath = operatepath

    def judgement(self):  # 判断该对文件执行的操作
        """注：
              0为清空文件内容。
              1为在文件中追加内容，保留原内容，在末尾追加。
              2为读取内容。"""

        if self.operationcode == 0:
            root_path = self.root_path
            # operate_path = "\\OperationalData\\Serialnumber.csv"
            FileOperations.purge_file(root_path, self.operate_path)  # 调用静态方法，并传入文件根目录
        if self.operationcode == 1:
            root_path = self.root_path
            operate_path = "\\OperationalData\\Serialnumber.csv"
            datas = self.content
            FileOperations.write_file(root_path, self.operate_path, datas)
        if self.operationcode == 2:
            root_path = self.root_path
            operate_path = "\\OperationalData\\Serialnumber.csv"
            reaturn_data = FileOperations.write_file(root_path, self.operate_path, datas)


class Button:
    """按钮控制"""

    def __init__(self):
        self.settings = Value_base()

    def mouse_button_one(self):
        pygame.init()
        # x_mouse, y_mouse = pyautogui.position()
        # for event in pygame.event.get():
        # if event.type == pygame.MOUSEBUTTONDOWN:
        x_mouse_clock, y_mouse_clock = pygame.mouse.get_pos()
        if 775 <= x_mouse_clock <= 1205 and 165 <= y_mouse_clock <= 190:
            return True
        else:
            return False  # , x_mouse_clock, y_mouse_clock

    def mouse_button_two(self):
        pygame.init()
        x_mouse_clock, y_mouse_clock = pygame.mouse.get_pos()
        if 105 <= x_mouse_clock <= 455 and 480 <= y_mouse_clock <= 580:
            return True
        else:
            return False

    def mouse_button_three(self):
        pygame.init()
        x_mouse_clock, y_mouse_clock = pygame.mouse.get_pos()
        if 1480 <= x_mouse_clock <= 1830 and 480 <= y_mouse_clock <= 580:
            return True
        else:
            return False


class Word_show:
    """"创建文字显示模块"""

    def __init__(self, guis, serial_number, space_information=None):
        self.settings = Value_base()
        self.word_paths = self.settings.word_path
        self.word_colors = self.settings.word_color
        # 从设置中导入相关参数

        self.guis = guis
        self.space_information = space_information
        self.serial_number = serial_number  # 通过数字确定显示什么部分

    def run_game(self):
        if self.serial_number == 1:
            #  文字显示----1
            word_left_one = pygame.font.Font(self.word_paths, 80)
            # 通过pygame.font.Font（）类从设置中获取字体路径，并渲染字体大小。进行实例化
            text_one = word_left_one.render("种子选择", True, self.word_colors)  # 传入要显示的文本，是否为平滑字体， 字体颜色，
            text_one_show = text_one.get_rect()  # 获取文本显示区域的大小
            text_one_show.center = (280, 530)  # 文本显示位置
            self.guis.blit(text_one, text_one_show)

        elif self.serial_number == 2:
            #  文字显示----2
            word_left_two = pygame.font.Font(self.word_paths, 80)
            # 通过pygame.font.Font（）类从设置中获取字体路径，并渲染字体大小。进行实例化
            text_two = word_left_two.render("种子编辑", True, self.word_colors)  # 传入要显示的文本，是否为平滑字体， 字体颜色，
            text_two_show = text_two.get_rect()  # 获取文本显示区域的大小
            text_two_show.center = (1650, 530)
            self.guis.blit(text_two, text_two_show)

        elif self.serial_number == 3:
            #  文字显示----3
            word_left_one = pygame.font.Font(self.word_paths, 50)
            # 通过pygame.font.Font（）类从设置中获取字体路径，并渲染字体大小。进行实例化
            text_one = word_left_one.render("你还未编辑任何种子！", True,
                                            self.word_colors)  # 传入要显示的文本，是否为平滑字体， 字体颜色，
            text_one_show = text_one.get_rect()  # 获取文本显示区域的大小
            text_one_show.center = (260, 530)
            self.guis.blit(text_one, text_one_show)

            word_left_one = pygame.font.Font(self.word_paths, 30)
            text_one = word_left_one.render("请前往模板进行编辑。", True, self.word_colors)
            text_one_show = text_one.get_rect()
            text_one_show.center = (240, 600)
            self.guis.blit(text_one, text_one_show)

        elif self.serial_number == 4:
            #  文字显示----4
            word_left_one = pygame.font.Font(self.word_paths, 60)
            # 通过pygame.font.Font（）类从设置中获取字体路径，并渲染字体大小。进行实例化
            text_two = word_left_one.render("请前往模板编辑", True, self.word_colors)  # 传入要显示的文本，是否为平滑字体， 字体颜色，
            text_two_show = text_two.get_rect()  # 获取文本显示区域的大小
            text_two_show.center = (1700, 540)
            self.guis.blit(text_two, text_two_show)

        # 种子选择界面文字
        elif self.serial_number == 5:
            # 解析相关信息
            seed_name = self.space_information[0]
            seed_place = self.space_information[1]
            # 文字显示----5
            word_left_one = pygame.font.Font(self.word_paths, 20)
            text_two = word_left_one.render(seed_name, True, self.word_colors)  # 传入要显示的文本，是否为平滑字体， 字体颜色，
            text_two_show = text_two.get_rect()  # 获取文本显示区域的大小
            text_two_show.center = seed_place
            self.guis.blit(text_two, text_two_show)


class List_bt:
    """关于种子选择列表"""

    def __init__(self, guis, information):
        #  从设置模块获取参数
        self.settings = Value_base()
        self.bt_much = self.settings.bt_much
        # self.bt_info = self.settings.bt_information

        #  从其他模块接受的参数
        self.guis = guis

        self.information = information

    def list_bt(self):
        left_size = self.information[0]
        top_size = self.information[1]
        width_size = self.information[2]
        hight_size = self.information[3]
        rect_one = pygame.Rect(left_size, top_size, width_size, hight_size)
        pygame.draw.rect(self.guis, (179, 179, 255, 100), rect_one)


class OrderRestrictions:
    """限制各个事件触发的顺序"""
    '''解决办法：
        将每个UI跳转与事件按照层级分配一个序列号，
        该序列号每两位表示一个层级，每次事件触发时
        检测序列号，将序列号切片进行层级分析，判断
        是否正确。
        '''

    def __init__(self, serialnumber):  # 接受参数序列号
        # 从设置导入参数
        self.settings = Value_base()
        self.root_path = self.settings.root_path

        # 接受初始化参数
        self.serialnumber = serialnumber

    def sequence_number_resolution(self):
        """序列号解析函数"""
        @staticmethod
        def data_write(serialnumber):
            """写入序列号"""
            operationcode = 1
            operate_path = "\\OperationalData\\Serialnumber.csv"
            FileOperations(operationcode, operate_path, serialnumber)
            
        
        @staticmethod  # 定义静态方法
        def data_get():
            # """该函数用于读取序列号（csv文件）并返回"""
            # path = self.root_path + "\\OperationalData\\Serialnumber.csv"  # 组合形成完整的根目录
            # with open(path, "a+", encoding="UTF-8") as f:  # 打开一个文件用于读写，并将其赋给一个对象f
              #   pass
              
            """该函数用来获取数据"""
            operationcode = 2
            operate_path = "\\OperationalData\\Serialnumber.csv"
            datas = FileOperations(operationcode, operate_path)
            datas = datas.judgement()
            return datas[-1]

            
        def makes(self):
            """控制函数
                负责调用所有方法。"""
            # data_write(self.serialnumber)
            serial = data_get()
            seriallen = len(serial)
            serialnumberlen = len(self.serialnumber)
            if serialnumberlen - seriallen == 2:
                if serial[2*seriallen-1:2*seriallen] == self.serialnumber[2 * seriallen - 1:2 * seriallen]:
                    pass
                else:
                    return False
            else:
                return False
            

    def judgment():
        """判断并返回结果"""
        pass
            
                



class Eventmakes:
    """关于鼠标键盘事件判断"""

    def __init__(self):
        # 从设置导入参数
        self.settings = Value_base()

        # 接受初始参数

    def quits(self):  # 退出函数
        for event in pygame.event.get():  # 遍历取出事件
            if event.type == pygame.QUIT:  # 判断事件类型，如果为点击×则执行
                pygame.quit()  # 退出pygame，卸载所有模块
                run = False  # 停止循环
                # sys.exit()  # 系统退出，终止程序


class Initiate:
    """创建启动页面"""

    def __init__(self):
        # 获取时间
        self.initiate_time = time.time()

        # 从设置模块获取相关设置参数
        self.settings = Value_base()
        self.ship = self.settings.ship
        self.game_name = self.settings.game_name
        self.image = self.settings.image
        self.word_paths = self.settings.word_path
        self.fps = self.settings.fps
        self.bt_much = self.settings.bt_much
        self.seed_info = self.settings.seed_info

    def initiate_gui(self):
        """创建启动页面函数"""

        pygame.init()  # 初始化pygame
        flags = pygame.RESIZABLE  # 设置窗口最大化
        guis = pygame.display.set_mode(self.ship, flags)  # 设置窗口大小
        pygame.display.set_caption(self.game_name)
        # bg_img = pygame.image.load(self.image).convert()
        # guis.blit(bg_img, (0, 0))

        pygame.display.update()  # 刷新
        fcclock = pygame.time.Clock()  # 设置刷新率
        run = True  # 固定代码段，实现点击"X"号退出界面的功能
        while run:
            # 循环获取事件，监听事件状态
            # backgroud_img = pygame.image.load(self.images)
            # guis.blit(backgroud_img, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # 判断用户是否点了"X"关闭按钮,并执行if代码段
                    pygame.quit()  # 卸载所有模块
                    run = False
                    # sys.exit()  # 终止程序，确保退出程序

                if event.type == VIDEORESIZE and shun_xu(1):  # 判断用户是否点击最大化按钮
                    SCREEN_SIZE = event.size  # 获取窗口大小
                    guis = pygame.display.set_mode(SCREEN_SIZE, flags)  # 重设窗口（在窗口最大化后）
                    bg_img = pygame.image.load(self.image).convert()  # 重设背景
                    guis.blit(bg_img, (0, 0))

                    pygame.display.update()  # 刷新

                if event.type == MOUSEBUTTONDOWN and MOUSEBUTTONUP:  # 判断用户是否点击鼠标
                    buttons = Button()
                    values_one = buttons.mouse_button_one()
                    values_two = buttons.mouse_button_two()
                    values_three = buttons.mouse_button_three()
                    # infoObject = pygame.display.Info()  # 获取屏幕大小
                    # print(infoObject)

                    # print(values_one, infoObject.current_w, infoObject.current_h)  # 第二个为输出屏幕长，第三个高
                    # 检测是否为顺序执行（防止前面内容覆盖后面的）

                    if values_one and shun_xu(2):
                        # print("成功")
                        # print(self.word_paths)
                        # 关键是这里！！！
                        # surface = guis.convert_alpha()  # 关键是这里！！！
                        # 关键是这里！！！
                        # surface.fill((255, 255, 255, 255))  # alpha=0,全透明
                        # 考虑图片
                        # 左方框
                        rect_one = pygame.Rect(105, 580, 350, 5)
                        pygame.draw.rect(guis, (94, 253, 253, 1), rect_one)
                        # 右方框
                        rect_two = pygame.Rect(1480, 580, 350, 5)
                        pygame.draw.rect(guis, (94, 253, 253, 1), rect_two)
                        # 此时你绘制的矩形将可以使用第四个数值的透明度值！！！！
                        # 绘制矩形（中第一个表示这个矩形画的容器在哪个地方，第二个参数表示采用什么颜色，第三个参数(前两个表示x轴的距离，y轴的距离，宽度，长度)，最后一个参数表示线的粗细(0表示一个实心的)）

                        #  文字显示----1
                        word_left_one = Word_show(guis, 1)
                        word_left_one.run_game()

                        #  文字显示----2
                        word_left_one = Word_show(guis, 2)
                        word_left_one.run_game()

                        fcclock.tick(self.fps)  # 刷新率设置
                        pygame.display.flip()  # 更新屏幕内容

                    elif values_two and shun_xu(3):
                        print("成功")
                        # 左方选择框
                        zero = 0

                        while zero <= self.bt_much and shun_xu(4):
                            # 左方选择框
                            rect_one = pygame.Rect(0, 0, 500, 1025)
                            pygame.draw.rect(guis, (229, 255, 249, 100), rect_one)
                            if self.bt_much != 0:
                                draw_number = 0

                                while draw_number <= self.bt_much:
                                    top_size = 70 * draw_number + 20
                                    information = [40, top_size, 400, 50]
                                    lists = List_bt(guis, information)
                                    lists.list_bt()
                                    # print("draw_number的值是：")
                                    # print(draw_number)
                                    # print(self.seed_info)
                                    seed_info_list = self.seed_info[:]

                                    one_seed = seed_info_list[draw_number]
                                    seed_name = one_seed[1]
                                    # seed_name = "seed_name"
                                    # seed_name_numder = len(seed_name)
                                    information = [seed_name, (240, top_size + 25)]
                                    word = Word_show(guis, 5, information)
                                    word.run_game()
                                    draw_number += 1

                            else:
                                #  文字显示----3
                                word = Word_show(guis, 3)
                                word.run_game()
                            fcclock.tick(self.fps)  # 刷新率设置

                            zero += 1
                            pygame.display.flip()  # 更新屏幕内容

                        fcclock.tick(self.fps)  # 刷新率设置
                        pygame.display.flip()  # 更新屏幕内容

                    elif values_three and shun_xu(5):
                        # print("成功22")
                        # 右方选择框
                        zero = True
                        while zero:
                            # 右方选择框
                            rect_one = pygame.Rect(1480, 0, 500, 1025)
                            pygame.draw.rect(guis, (229, 255, 249, 100), rect_one)

                            #  文字显示----2
                            word = Word_show(guis, 4)
                            word.run_game()

                            zero = False

                        fcclock.tick(self.fps)  # 刷新率设置
                        pygame.display.flip()  # 更新屏幕内容
