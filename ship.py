# create module ship, which contains class Ship(), that manages the behavior of the ship

import pygame

class Ship():
    def __init__(self, screen): 
        self.screen = screen
        
        #loading the image and get its rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    def blitme(self):
        # blit function allows you to draw one surface onto another
        self.screen.blit(self.image, self.rect)
        
        
        
