
import pygame

from setting import Value_base


class Gui:

    def __init__(self):
        self.settings = Value_base()
        self.game_name = self.settings.game_name
        self.image = self.settings.image
        self.ship = self.settings.ship
        self.gui = self.game_gui

    def game_gui(self):
        """游戏界面gui"""
        pygame.init()
        pygame.display.set_caption(self.game_name)
        run = True
        while run:
            for event in pygame.event.get():
                screen_size = event.size
                guis = pygame.display.set_mode(screen_size)
                gui_bmp = self.gui
                guis.blit(gui_bmp, (0, 0))
                pygame.display.update()










