#!/usr/bin/env python
#-*- coding:utf-8 -*-

import pygame
import sys

from game.game import Game
from menu.menu import Menu



SIZE = WIDTH, HEIGHT = 1100, 1000
FRAMERATE = 60
clock = pygame.time.Clock()



#set up the window
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('THpy')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

menu = Menu(screen)

state = 1
running = True
while running:
    match state:
        case 0:
            running = False
        case 1:
            state = menu.update(screen)
        case 2:
            state = game.update(screen)
        case 3:
            game = Game((700, 960), (20, 20))
            state = 2
    pygame.display.update()
    clock.tick(FRAMERATE)

sys.exit()

