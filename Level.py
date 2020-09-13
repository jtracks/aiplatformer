'''
Contains the level basic class, Levels will inherit from this class to make a level
'''

import pygame as pg
import random
from itertools import chain
from Config import SCREEN, BACKGROUND, TERRAIN
from AssetLoader import BACKGROUNDS, TERRAINS

SCREEN_WIDTH, SCREEN_HIGHT = SCREEN['SIZE']

class Level():
    ''' Default level '''
    
    level_limit = -1000
    world_shift = 0
    tick = 0

    def __init__(self, player, lvl_type='Blue',  ter_type='Wood'):

        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.bots = pg.sprite.Group()
        self.player = player
        self.level_type = lvl_type
        self.terrain_type = ter_type

        for width, height, x, y in self._platforms():
            self.platforms.add(Platform(width, height, x, y, ter_type))

    def _platforms(self):
        ''' Platform(width, height, x, y) '''

        ground = (5000, 96, self.level_limit, SCREEN_HIGHT - 64)
        left_block = (64, SCREEN_HIGHT-64, self.level_limit, 0)
        right_block = (64, SCREEN_HIGHT-500, 1600, 100)
        roof =(5000, 64, self.level_limit, - 64)
        wall = (96, 200, 1000, SCREEN_HIGHT - 550)
        big_block = (320, 160, 1200, SCREEN_HIGHT - 500)
        platform1 = (210, 70, 600, SCREEN_HIGHT - 200)
        platform2 = (210, 70, 600, SCREEN_HIGHT - 600)

        return [ground, left_block, right_block, roof, wall, big_block, platform1, platform2]


    def update(self):
        ''' Update everything '''

        self.platforms.update()
        self.enemies.update()

    def draw(self, screen):
        ''' Draw content on screen '''
        
        if self.tick == 60:
            self.tick = 0

        offset = (BACKGROUND['SIZE'][0]*(self.tick/60-1), BACKGROUND['SIZE'][0]*(self.tick/60-1))

        screen.blit(BACKGROUNDS[self.level_type], offset)

        self.platforms.draw(screen)
        self.enemies.draw(screen)

        self.tick += 1
    
    def shift_world(self, speed_x):
        ''' Scroll world '''

        self.world_shift += speed_x

        for item in chain(self.platforms, self.enemies, self.bots):
            item.rect.x += speed_x

class Platform(pg.sprite.Sprite):
    ''' Platform the player can jump on '''
 
    def __init__(self, width, height, x, y, ter_type='Wood'):
        
        super(Platform,self).__init__()
        width -= (width % TERRAIN['SIZE'][0])
        height -= (height % TERRAIN['SIZE'][1])
        self.image = pg.Surface([width, height])

        self._add_terrain(width, height, ter_type)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def _add_terrain(self, width, height, ter_type):
        
        terrain = TERRAINS[ter_type]
        ter_w, ter_h = TERRAIN['SIZE']

        # Add fill to every square
        for w in range(0, width+1 , ter_w):
            for h in range(0, height+1 , ter_h):
                self.image.blit(random.choice(terrain['FILL']),(w,h))

        # Add tops and bottoms
        for w in range(0, width+1 , ter_w):
            self.image.blit(terrain['TOP'], (w, 0))
            self.image.blit(terrain['BOTTOM'], (w, height-ter_h))

        # Add left and rights
        for h in range(0, height+1 , ter_h):
            self.image.blit(terrain['LEFT'], (0, h))
            self.image.blit(terrain['RIGHT'], (width-ter_w, h))
        
        # Add corners 
        self.image.blit(terrain['TOP LEFT'], (0, 0))
        self.image.blit(terrain['TOP RIGHT'], (width-ter_w, 0))
        self.image.blit(terrain['BOTTOM LEFT'], (0, height-ter_h))
        self.image.blit(terrain['BOTTOM RIGHT'], (width-ter_w, height-ter_h))
        