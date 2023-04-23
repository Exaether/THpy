# !/usr/bin/env python
# -*- coding:utf-8 -*-

import pygame

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, pos, speed, image):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = speed
    
    def update(self, screen):
        """
        update the bullet and delete it if it go OOB
        
        parameters
        ----------
        screen: pygame.Surface
            the screen on wich the bullet is
        
        returns
        -------
            None
        """
        width, height = screen.get_rect().size
        if (self.rect.top >= height
                or self.rect.bottom <= 0
                or self.rect.left >= width
                or self.rect.right <= 0
                ):
            self.kill()
        self.rect.move_ip(*self.speed)

