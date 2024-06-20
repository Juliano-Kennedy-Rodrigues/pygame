#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH

pygame.init()


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load('./asset/menuBG.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer.init()
        pygame.mixer_music.load('./asset/menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Crab", (0, 0, 100), ((WIN_WIDTH/2), 70))
            self.menu_text(50, "Shooter", (0, 0, 100), ((WIN_WIDTH / 2), 110))
            pygame.display.flip()
        pass

# método que cria os textos no menu
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_centre_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_centre_pos)
        self.window.blit(source=text_surf, dest=text_rect)
