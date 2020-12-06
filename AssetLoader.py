import pygame as pg
from PIL import Image
from os.path import join
from Config import *
import random

load = pg.image.load

def load_asset(path, size_tuple, length_tuple=(1,1)):
    ''' Returns a list of surfaces with (len = length, size = size_tuple)'''
   
    if length_tuple == (1,1):
        bitmap = pg.image.load(path)
        return [pg.transform.scale(bitmap, size_tuple)]

    else:
        bmps = Image.open(path,)
        width, height = bmps.width / length_tuple[0], bmps.height / length_tuple[1]
        surface_list = []

        for y in range(length_tuple[1]):
            for x in range(length_tuple[0]):
                box = bmps.crop((width*x, height*y, width*(x+1), height*(y+1)))
                surf = pg.image.fromstring(box.tobytes(), box.size, 'RGBA')
                surf = pg.transform.scale(surf, size_tuple)
                surface_list.append(surf)

        return surface_list  

def fill_background(bgr_image):

    sw, sh = SCREEN['SIZE']
    bw, bh = bgr_image[0].get_size()

    background = pg.Surface((sw + 2*bw, sh + 2*bh))

    for x in range(int(sw/bw) + 2):
        for y in range(int(sh/bh) + 2 ):
            background.blit(bgr_image[0], (x*bw, y*bh))  

    return background 

PATH_TO_CHAR = join('assets', 'Main_Characters')
PATH_TO_BACKGROUND = join('assets', 'Background')
PATH_TO_TERRAIN = join('assets', 'Terrain')
PATH_TO_ITEMS = join('assets','Items','Fruits')
PATH_TO_CHECKPOINTS = join('assets','Items','Checkpoints','Checkpoint')

# Animations for the main character
ANIMATIONS_CHAR = {}
for character in MAIN_CHARACTER['NAME']:

    ANIMATIONS_CHAR[character] = {
        'DOUBLE JUMP': load_asset(join(PATH_TO_CHAR, character, 'Double_Jump_(32x32).png'), MAIN_CHARACTER['SIZE'], (6, 1)),
        'FALL': load_asset(join(PATH_TO_CHAR, character, 'Fall_(32x32).png'), MAIN_CHARACTER['SIZE'], (1, 1)),
        'HIT': load_asset(join(PATH_TO_CHAR, character, 'Hit_(32x32).png'), MAIN_CHARACTER['SIZE'], (7, 1)),
        'IDLE': load_asset(join(PATH_TO_CHAR, character, 'Idle_(32x32).png'), MAIN_CHARACTER['SIZE'], (11, 1)),
        'JUMP': load_asset(join(PATH_TO_CHAR, character, 'Jump_(32x32).png'), MAIN_CHARACTER['SIZE'], (1, 1)),
        'RUN': load_asset(join(PATH_TO_CHAR, character, 'Run_(32x32).png'), MAIN_CHARACTER['SIZE'], (12, 1)),
        'WALL JUMP': load_asset(join(PATH_TO_CHAR, character, 'Wall_Jump_(32x32).png'), MAIN_CHARACTER['SIZE'], (5, 1))
    }

# Background tiles
BACKGROUNDS = {}
for bgr in BACKGROUND['NAME']:
    BACKGROUNDS[bgr] = fill_background(load_asset(join(PATH_TO_BACKGROUND, f'{bgr}.png'), BACKGROUND['SIZE'], (1,1)))

# Collectibles 
COLLECTIBLES = {}
for item in COLLECTIBLE['NAME']:
    COLLECTIBLES[item] = load_asset(join(PATH_TO_ITEMS,'Apple.png'),COLLECTIBLE['SIZE'],(17,1))

CHECKPOINTS = {}
for item in CHECKPOINT['NAME']: 
    CHECKPOINTS[item] = load_asset(join(PATH_TO_CHECKPOINTS,'Checkpoint_(Flag_Out)_(64x64).png'),CHECKPOINT['SIZE'],(26,1))


# Load terrains, kinda weirdly done but works
t = load_asset(join(PATH_TO_TERRAIN,'Terrain_(16x16).png'),TERRAIN['SIZE'], (22,11))
TERRAINS = {}
for terrain_name, offset  in zip(TERRAIN['NAME'], TERRAIN['OFFSET']):
    TERRAINS[terrain_name] = {
        'TOP LEFT':  t[0 + offset],
        'TOP': t[1 + offset],
        'TOP RIGHT': t[2 + offset],
        'LEFT': t[22 + offset],
        'RIGHT': t[24 + offset],
        'BOTTOM LEFT': t[44 + offset],
        'BOTTOM': t[45 + offset],
        'BOTTOM RIGHT': t[46 + offset],
        'FILL': [t[23 + offset]] #, t[3 + offset], t[4 + offset], , t[25 + offset], t[26 + offset]]
    }

