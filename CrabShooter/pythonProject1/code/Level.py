#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, menu_option, name):
        self.window = window
        self.name = name
        self.mode = menu_option  # opção do menu
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run(self, ):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('loop end')
                    pygame.quit()
                    sys.exit()
        pass

