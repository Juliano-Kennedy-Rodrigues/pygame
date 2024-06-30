#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image
from pygame import Surface


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf: Surface = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    # classes filhas de entity obrigatoriamente implementam esse método
    @abstractmethod
    def move(self, ):
        pass
