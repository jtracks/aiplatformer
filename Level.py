
import pygame as pg
from itertools import chain
from Config import SCREEN
from AssetLoader import BACKGROUNDS

SCREEN_WIDTH, SCREEN_HIGHT = SCREEN['SIZE']

class Level():
    ''' Default level '''
    
    level_limit = -1000
    world_shift = 0

    def __init__(self, player, platforms=[(210, 70, 600, 400)], lvl_type='BLUE'):

        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = player
        self.level_type = lvl_type

        ground = (5000, 40, self.level_limit, SCREEN_HIGHT - 40)
        wall = (80, 400, 1000, 50)

        for width, height, x, y in chain([ground, wall], platforms):
            self.platforms.add(Platform(width, height, x, y))

    def update(self):
        ''' Update everything '''

        self.platforms.update()
        self.enemies.update()

    def draw(self, screen):
        ''' Draw content on screen '''

        screen.blit(BACKGROUNDS[self.level_type], (0, 0))

        self.platforms.draw(screen)
        self.enemies.draw(screen)
    
    def shift_world(self, speed_x):
        ''' Scroll world '''

        self.world_shift += speed_x

        for item in chain(self.platforms, self.enemies):
            item.rect.x += speed_x

class Platform(pg.sprite.Sprite):
    ''' Platform the player can jump on '''
 
    def __init__(self, width, height, x, y, bgr_type='BLUE'):
        
        super(Platform,self).__init__()
        self.image = pg.Surface([width, height])
        self.image.fill((0,200,0))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    