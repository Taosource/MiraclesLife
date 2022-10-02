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

    def mouse_first_button(self):
        pygame.init()
        # x_mouse, y_mouse = pyautogui.position()
        # for event in pygame.event.get():
            # if event.type == pygame.MOUSEBUTTONDOWN:
        x_mouse_clock, y_mouse_clock = pygame.mouse.get_pos()
        if 775 <= x_mouse_clock <= 1205 and 165 <= y_mouse_clock <= 190:
            return True
        else:
            return False, x_mouse_clock, y_mouse_clock

class Initiate:
    """创建启动页面"""

    def __init__(self):
        self.initiate_time = time.time()
        # 获取时间

        self.settings = Settings()
        self.ship = self.settings.ship
        self.game_name = self.settings.game_name
        self.image = self.settings.image

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
                    values_1 = buttons.mouse_first_button()
                    infoObject = pygame.display.Info()
                    # print(values_1, infoObject.current_w, infoObject.current_h)  # 第二个为输出屏幕长，第三个高
                    if values_1 == True:
                        print("成功")
