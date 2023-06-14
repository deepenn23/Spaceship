# create module ship, which contains class Ship(), that manages the behavior of the ship

import pygame


class Ship():
    
     # we take in a screen param when calling Ship beacuase ship needs a screen to be displayed on
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        
        #loading the image and get its rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()  # image rectangle => represents position and size
        self.screen_rect = screen.get_rect()  #screen rectangle
        
        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        
        # Movement flag
        self.moving_right = False
        self.moving_left = False
        
        
        #update usually updates the posiiton of the ship
    def update(self):
        """Update the ship's position based on the movement flag.""" 
        ## allows us to stay within the screen
        ## if the ship is moving right and the ship hasnt touch the screen
        ##     move the ship to the right with 1.5x speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
           self.center += self.ai_settings.ship_speed_factor
        ## if the ship is moving left and hasnt touch the screen
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            
        self.rect.centerx = self.center
    
    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx
        
    def blitme(self):
        # blit function allows you to draw one surface onto another
        self.screen.blit(self.image, self.rect)
        
        
        
