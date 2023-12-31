
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats

def run_game():
    #intialize game and create the screen object
    '''settings are in the setting.py'''
    pygame.init() 
    ai_settings = Settings() 
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(ai_settings ,screen) #
    # Make a group to store bullets in.
    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_settings)
    #create a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    
    
# listen for any events from the user
    while True:
       gf.check_events(ai_settings, screen, ship, bullets)
       if stats.game_active:
            ship.update()
            gf.update_bullets(bullets ,screen, ai_settings, ship, aliens)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            
       gf.update_screen(ai_settings, screen, ship, aliens, bullets)
       

run_game()






