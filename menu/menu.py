# !/usr/bin/env python
# -*- coding:utf-8 -*-

import pygame

from .button import Button

class Menu:
    """
    the game's menu
    
    attributes
    ----------
    play: Button
        the play button
    quit: Button
        the quit button
    
    methods
    -------
    update(screen) -> int
        update the menu and display it
    """
    
    def __init__(self, screen):
        """
        constructor of the Menu class
        set up the attributes
        
        parameters
        ----------
        None
        
        returns
        -------
        None
        """
        width, height = screen.get_rect().size
        self.play = Button(
            (
                width//2 - 100,
                height//3 - 30,
                200,
                60
            ),
            "play",
            (255, 0, 0)
        )
        self.quit = Button(
            (
                width//2 - 100,
                height*(2/3) - 30,
                200,
                60
            ),
            "quit",
            (255, 0, 0)
        )
    
    def update(self, screen):
        """
        update the menu and display it on the screen
        
        parameters
        ----------
        screen: pygame.Surface
            the screen
        
        returns
        -------
        int
            the next state
        """
        mousepos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    return 0
                case pygame.MOUSEBUTTONUP:
                    if self.play.mouse_on(mousepos):
                        screen.fill((0, 0, 0))
                        return 3
                    if self.quit.mouse_on(mousepos):
                        return 0
        
        screen.fill((0, 0, 0))
        self.play.display(screen, mousepos)
        self.quit.display(screen, mousepos)
        return 1

