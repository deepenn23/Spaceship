
class Settings():
# a class to store all setting for the game
    def __init__(self):
        #intialize the setting for the screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255,255, 255)
        self.ship_speed_factor = 1.5
        self.ship_limit = 2

        
        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
        # Alien settings
        self.alien_speed_factor = 5
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
        
   


