# !/usr/bin/env python
# -*- coding:utf-8 -*-

import pygame
from math import cos, sin
from typing import Tuple


class Player(pygame.sprite.Sprite):
    """
        a player that can move on the screen and shoot bullets
        
        attributes
        ----------
        rect: pygame.Rect
            the rect of the sprite
        image: pygame.Surface
            the image
        mask: pygame.Mask
            the mask used for collides
        up, down, right, left: bool
            enable moving in one direction
        speed: int
            the size of a displacement
        
        methods
        -------
        update(screen):
            update the player
    """
    def __init__(self, pos: Tuple[int], image):
        """
        constructor of the Player class
        set up the attributes
        """
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.hitbox = pygame.image.load('hitbox.png')
        self.mask = pygame.mask.from_surface(self.hitbox)
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        self.speed = 4
        self.focus = False
    
    def draw(self, screen):
        """
        draw the sprite on a given surface
        
        parameters
        ----------
        screen: pygame.Surface
            the surface to draw the sprite on
        
        returns
        -------
        None
        """
        screen.blit(self.image, self.rect)
        
        if self.focus:
            screen.blit(self.hitbox, self.rect)
    
    def update(self, screen):
        """
        update the pos of the player depending on wich move is enabled
        
        parameters
        ----------
        None
        
        returns
        -------
        None
        """
        width, height = screen.get_rect().size
        
        if self.up and (self.rect.top - self.speed > 0):
            self.rect.center = (
                self.rect.center[0],
                self.rect.center[1] - self.speed
            )
        if self.down and (self.rect.bottom + self.speed < height):
            self.rect.center = (
                self.rect.center[0],
                self.rect.center[1] + self.speed
            )
        if self.right and (self.rect.right + self.speed < width):
            self.rect.center = (
                self.rect.center[0] + self.speed,
                self.rect.center[1]
            )
        if self.left and (self.rect.left - self.speed > 0):
            self.rect.center = (
                self.rect.center[0] - self.speed,
                self.rect.center[1]
            )

