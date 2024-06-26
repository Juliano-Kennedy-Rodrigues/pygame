#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW

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
        menu_option = 0
        while True:
            # desenhar na tela
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Crab", (0, 0, 100), ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", (0, 0, 100), ((WIN_WIDTH / 2), 110))
            # esse for deixa as legendas amarelas quando seleciona elas com as setinhas
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, (WIN_WIDTH / 2, 200 + 30 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, (WIN_WIDTH / 2, 200 + 30 * i))
            pygame.display.flip()

            # verificar eventos
            # esse evento faz a tela (window) encerrar. Fecha o jogo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('loop end')
                    pygame.quit()
                    sys.exit()
                # esse evento identifica  a tecla clicada
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option <= len(MENU_OPTION) - 2:
                            menu_option += 1
                        else:
                            menu_option = 0
                # esse evento identifica  a tecla clicada
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    # método que cria os textos no menu
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_centre_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_centre_pos)
        self.window.blit(source=text_surf, dest=text_rect)
