# !/usr/bin/env python
# -*- coding:utf-8 -*-


import pygame
import pygame.freetype


class Button:
    """
    modelize a button in order to display it and test the clic
    
    attributes
    ----------
    rect: pygame.Rect
        the area of display
    text: str
        the text to display
    font: pygame.freetype.Font
        the font
    color: tuple
        the color of the button
    
    methods
    -------
    display(screen, pos)
        display the button
    mouse_on(pos)
        test if the mouse is on the button
    """
    
    def __init__(self, area, text, color):
        """
        constructor of the button class
        set up the attributes
        
        parameters
        ----------
        area: tuple
            the area (x, y, width, height)
        text: str
            the text of the button
        color: tuple
            the color...
        
        returns
        -------
        None
        """
        pygame.freetype.init()
        self.rect = pygame.Rect(area)
        self.text = text
        self.color = color
        self.font = pygame.freetype.Font("VCR_OSD_MONO.ttf", size= 30)
    
    def display(self, screen, pos):
        """
        display the button on the given screen, and add a circle if the
        mose is on
        
        parameters
        ----------
        screen: pygame.Surface
            the surface to display on
        pos: tuple
            the pos of the mouse
        
        returns
        -------
        None
        """
        image = pygame.Surface(self.rect.size)
        image.fill(self.color)
        text_surf, text_rect = self.font.render(self.text)
        text_rect.center = (
            self.rect.center[0] - self.rect.left,
            self.rect.center[1] - self.rect.top
        )
        image.blit(text_surf, text_rect)
        
        #if the mouse is on the button
        if self.mouse_on(pos):
            #then we draw 2 circles around the text
            pygame.draw.circle(
                image,
                (0, 0, 0),
                (text_rect.left - 20, text_rect.center[1]),
                15
            )
            pygame.draw.circle(
                image,
                (0, 0, 0),
                (text_rect.right + 20, text_rect.center[1]),
                15
            )
        #and finally, past the image on the area
        screen.blit(image, self.rect)
    
    def mouse_on(self, pos):
        """
        test if the pouse is on the button's area
        
        parameters
        ----------
        pos: tuple
            the pos of the mouse
        
        returns
        -------
        bool
        """
        return self.rect.collidepoint(pos)

