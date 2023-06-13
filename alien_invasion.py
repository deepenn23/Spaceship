
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #intialize game and create the screen object
    '''settings are in the setting.py'''
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(screen)

# listen for any events from the user
    while True:
       gf.check_events()
       gf.update_screen(ai_settings, screen, ship)
       

run_game()






