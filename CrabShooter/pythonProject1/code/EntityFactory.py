#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import BG_ARRAY, WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            # criando o background da Fase1
            case 'Level1Bg':
                list_bg = []
                for i in range(len(BG_ARRAY)):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            # para instanciar os jogadores
            case 'Player1':
                return Player('Player1', (5, WIN_HEIGHT-110))
            case 'Player2':
                return Player('Player2', (5, WIN_HEIGHT-210))

            # para instanciar os inimigos
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 30, random.randint(0, WIN_HEIGHT)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 130, random.randint(0, WIN_HEIGHT)))
