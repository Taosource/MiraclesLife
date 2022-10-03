import pyautogui
import pygame  # 导入pygame包
import time
import sys

from pygame import VIDEORESIZE
from pygame.constants import FULLSCREEN, SCALED, MOUSEBUTTONDOWN, MOUSEBUTTONUP

# 自己的
from setting import Value_base


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
        self.serial_number = serial_number

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
        self.bt_info = self.settings.bt_information

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


class Initiate:
    """创建启动页面"""

    def __init__(self):
        self.initiate_time = time.time()
        # 获取时间
        self.settings = Value_base()
        self.ship = self.settings.ship
        self.game_name = self.settings.game_name
        self.image = self.settings.image
        self.word_paths = self.settings.word_path
        self.fps = self.settings.fps
        self.bt_much = self.settings.bt_much
        # 从设置模块获取相关设置参数

    def initiate_gui(self):
        """创建启动页面函数"""

        global shuns, shun
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
                # ab = Button(1)
                # print(ab.mouse())

                if event.type == pygame.QUIT:  # 判断用户是否点了"X"关闭按钮,并执行if代码段
                    pygame.quit()  # 卸载所有模块
                    run = False
                    # sys.exit()  # 终止程序，确保退出程序

                if event.type == VIDEORESIZE:  # 判断用户是否点击最大化按钮
                    SCREEN_SIZE = event.size  # 获取窗口大小

                    guis = pygame.display.set_mode(SCREEN_SIZE, flags)  # 重设窗口（在窗口最大化后）
                    bg_img = pygame.image.load(self.image).convert()  # 重设背景
                    guis.blit(bg_img, (0, 0))

                    pygame.display.update()  # 刷新
                    shuns = 0

                if event.type == MOUSEBUTTONDOWN and MOUSEBUTTONUP:  # 判断用户是否点击鼠标
                    buttons = Button()
                    values_one = buttons.mouse_button_one()
                    values_two = buttons.mouse_button_two()
                    values_three = buttons.mouse_button_three()
                    infoObject = pygame.display.Info()  # 获取屏幕大小

                    print(values_one, infoObject.current_w, infoObject.current_h)  # 第二个为输出屏幕长，第三个高
                    # 检测是否为顺序执行（防止前面内容覆盖后面的）

                    if shuns <= 1:
                        shun = True

                    if shuns >= 1:
                        shun = False

                    if values_one and shun:
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

                    elif values_two:
                        print("成功")
                        shuns += 1
                        # 左方选择框
                        zero = 0
                        while zero <= self.bt_much:
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
                                    draw_number += 1

                                    seed_name = "seed_name"
                                    seed_name_numder = len(seed_name)
                                    information = [seed_name, (240, top_size+25)]
                                    word = Word_show(guis, 5, information)
                                    word.run_game()

                            else:
                                #  文字显示----3
                                word = Word_show(guis, 3)
                                word.run_game()
                            fcclock.tick(self.fps)  # 刷新率设置
                            pygame.display.flip()  # 更新屏幕内容

                            zero += 1

                        fcclock.tick(self.fps)  # 刷新率设置
                        pygame.display.flip()  # 更新屏幕内容

                    elif values_three:
                        print("成功22")
                        shuns += 1
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
