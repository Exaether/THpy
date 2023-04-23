# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
this module contain a class that represent a game, with all its attributes
like the game surface, player, enemiess, and more

classes
-------
    - Game
"""

import pygame
from typing import Tuple

from .player import Player
from .bullets import Bullet

#colors
BLACK = 0, 0, 0
BLUE = 0, 0, 255

class Game:
    """
    represent an instance of game that handle a frame of this game
    
    attributes
    ----------
    player: Player
        yup, you got it
    bullets: pygame.sprite.Group
        all bullets on the screen
    screen: pygame.Surface
        the surface to draw the game on
    """
    
    def __init__(self, size: Tuple[int], pos: Tuple[int]):
        """
        constructor of the Game class
        
        parameters
        ----------
        size: Tuple[int]
            (width, height) the size of the game surface
        pos: Tuple[int]
            (posx, posy) the pos of the up-right corner on the game rect
        
        returns
        -------
        None
        """
        self.surf = pygame.Surface(size)
        self.rect = pygame.Rect(*pos, *size)
        playerpos = (
            size[0]//2,
            size[1]*2 // 3
        )
        self.player = Player(playerpos, 'mokou.png')
        bulletpos = (
            size[0]//2,
            size[1]//3
        )
        bullets = [
            Bullet(bulletpos, (-1, 1), 'bullet.png'),
            Bullet(bulletpos, (0, 1), 'bullet.png'),
            Bullet(bulletpos, (1, 1), 'bullet.png')
        ]
        self.bullets = pygame.sprite.Group(*bullets)
        self.pause = False
    
    def draw(self, screen):
        """
        draw the game on the given screen
        
        parameters
        ----------
        None
        
        returns
        -------
        None
        """
        self.surf.fill(BLUE)
        self.player.draw(self.surf)
        self.bullets.draw(self.surf)
        
        screen.blit(self.surf, self.rect)
    
    def update(self, screen):
        """
        simulate a frame of the game and display it on the give surface
        
        parameters
        ----------
        screen: pygame.Surface
            the surface to display on
        
        returns
        -------
        int
            the next state
            0 to quit; 1 to continue
        """
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    return 0
                
                case pygame.KEYDOWN:
                    if not self.pause:
                        match event.key:
                            case pygame.K_UP:
                                self.player.up = True
                            case pygame.K_DOWN:
                                self.player.down = True
                            case pygame.K_LEFT:
                                self.player.left = True
                            case pygame.K_RIGHT:
                                self.player.right = True
                            case pygame.K_LSHIFT:
                                self.player.focus = True
                                self.player.speed //= 2
                
                case pygame.KEYUP:
                    if not self.pause:
                        match event.key:
                            case pygame.K_UP:
                                self.player.up = False
                            case pygame.K_DOWN:
                                self.player.down = False
                            case pygame.K_LEFT:
                                self.player.left = False
                            case pygame.K_RIGHT:
                                self.player.right = False
                            case pygame.K_LSHIFT:
                                self.player.focus = False
                                self.player.speed *= 2
        
        if pygame.sprite.spritecollide(
                self.player,
                self.bullets,
                True,
                collided = pygame.sprite.collide_mask
                ):
            pass
        
        screen.fill(BLACK)
        self.player.update(self.surf)
        self.bullets.update(self.surf)
        self.draw(screen)
        return 2

