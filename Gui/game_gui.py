# 导入外部第三方库
import pygame
from pygame.locals import *
import sys

# 导入自己的包
from setting import Value_base


class EventMake:
    def __init__(self):
        pass

    def quits(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                sys.excit()
            else:
                pass
                
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
        screen = pygame.display.set_mode((1920, 1027), RESIZABLE)
        gui = pygame.image.load(self.gui).convert()

        run = True
        while run:
            EventMake = EventMake()
            EventMake.quit()


