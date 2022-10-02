import pyautogui
import pygame  # 导入pygame包
import time
import sys

from pygame import VIDEORESIZE
from pygame.constants import FULLSCREEN, SCALED, MOUSEBUTTONDOWN, MOUSEBUTTONUP

# 自己的
from setting import Settings


class Button:
    """按钮控制"""

    def __init__(self):
        self.settings = Settings()

        self.x_mouse_clock = 0
        self.y_mouse_clock = 0

    def mouse_button(self):
        pygame.init()
        # x_mouse, y_mouse = pyautogui.position()
        # for event in pygame.event.get():
        # if event.type == pygame.MOUSEBUTTONDOWN:
        x_mouse_clock, y_mouse_clock = pygame.mouse.get_pos()
        if 775 <= x_mouse_clock <= 1205 and 165 <= y_mouse_clock <= 190:
            return True
        else:
            return False  # , x_mouse_clock, y_mouse_clock


class Initiate:
    """创建启动页面"""

    def __init__(self):
        self.initiate_time = time.time()
        # 获取时间
        self.settings = Settings()
        self.ship = self.settings.ship
        self.game_name = self.settings.game_name
        self.image = self.settings.image
        self.word_paths = self.settings.word_path
        self.fps = self.settings.fps
        # 从设置模块获取相关设置参数

        # 结束函数

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
                elif event.type == MOUSEBUTTONDOWN and MOUSEBUTTONUP:  # 判断用户是否点击鼠标
                    buttons = Button()
                    values_1 = buttons.mouse_button()
                    infoObject = pygame.display.Info()  # 获取屏幕大小
                    # print(values_1, infoObject.current_w, infoObject.current_h)  # 第二个为输出屏幕长，第三个高
                    if values_1:
                        print("成功")
                        # print(self.word_paths)

                        # 关键是这里！！！
                        # surface = guis.convert_alpha()  # 关键是这里！！！
                        # 关键是这里！！！
                        # surface.fill((255, 255, 255, 255))  # alpha=0,全透明
                        # 左方框
                        rect_one = pygame.Rect(105, 480, 350, 100)
                        pygame.draw.rect(guis, (255, 255, 255, 255), rect_one)
                        # 右方框
                        rect_two = pygame.Rect(1480, 480, 350, 100)
                        pygame.draw.rect(guis, (255, 255, 255, 255), rect_two)
                        # 此时你绘制的矩形将可以使用第四个数值的透明度值！！！！
                        # 绘制矩形（中第一个表示这个矩形画的容器在哪个地方，第二个参数表示采用什么颜色，第三个参数(前两个表示x轴的距离，y轴的距离，宽度，长度)，最后一个参数表示线的粗细(0表示一个实心的)）

                        #  文字显示----1
                        word_left_one = pygame.font.Font(self.word_paths, 80)
                        # 通过pygame.font.Font（）类从设置中获取字体路径，并渲染字体大小。进行实例化
                        text_one = word_left_one.render("种子选择", True, (102, 217, 255))  # 传入要显示的文本，是否为平滑字体， 字体颜色，
                        text_one_show = text_one.get_rect()  # 获取文本显示区域的大小
                        text_one_show.center = (280, 530)
                        guis.blit(text_one, text_one_show)
                        #  文字显示----2
                        word_left_one = pygame.font.Font(self.word_paths, 80)
                        # 通过pygame.font.Font（）类从设置中获取字体路径，并渲染字体大小。进行实例化
                        text_one = word_left_one.render("种子编辑", True, (102, 217, 255))  # 传入要显示的文本，是否为平滑字体， 字体颜色，
                        text_one_show = text_one.get_rect()  # 获取文本显示区域的大小
                        text_one_show.center = (1650, 530)
                        guis.blit(text_one, text_one_show)

                        fcclock.tick(self.fps)  # 刷新率设置
                        pygame.display.flip()  # 更新屏幕内容
