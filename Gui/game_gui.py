import pygame
from setting import Value_base
from pygame.locals import *

class Gui:
    def __init__(self):
        self.settings = Value_base()
        self.game_name = self.settings.game_name
        self.ship = self.settings.ship
        self.gui = self.settings.game_gui

    def game_gui(self):
        """游戏界面gui"""
        pygame.init()
        pygame.display.set_caption(self.game_name)
        screen = pygame.display.set_mode((1920, 1027), FULLSCREEN, 32)
        gui = pygame.image.load(self.gui).convert()

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # 判断用户是否点了"X"关闭按钮,并执行if代码段
                    pygame.quit()
                    run = False
                screen.blit(gui, (0, 0))
                pygame.display.update()

game_gui = Gui()
game_gui.game_gui()

