import pygame as pg
from PIL import Image
from os.path import join
from Config import *

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

        for x in range(length_tuple[0]):
            for y in range(length_tuple[1]):
                box = bmps.crop((width*x, height*y, width*(x+1), height*(y+1)))
                box = box.resize(size_tuple)
                surf = pg.image.fromstring(box.tobytes(), size_tuple, 'RGBA')
                surface_list.append(surf)

        return surface_list  

def fill_background(bgr_image):

    sw, sh = SCREEN['SIZE']
    bw, bh = bgr_image[0].get_size()

    background = pg.Surface((sw, sh))

    for x in range(int(sw/bw)):
        for y in range(int(sh/bh)):
            background.blit(bgr_image[0], (x*bw, y*bh))  

    return background 

PATH_TO_CHAR = join('assets', 'Main Characters', MAIN_CHARACTER['NAME'])
PATH_TO_BACKGROUND = join('assets', 'Background')
PATH_TO_TERRAIN = join('assets', 'Terrain')

# Animations for the main character
ANIMATIONS_MAIN_CHAR = {
    'DOUBLE JUMP': load_asset(join(PATH_TO_CHAR, 'Double Jump (32x32).png'), MAIN_CHARACTER['SIZE'], (6, 1)),
    'FALL': load_asset(join(PATH_TO_CHAR, 'Fall (32x32).png'), MAIN_CHARACTER['SIZE'], (1, 1)),
    'HIT': load_asset(join(PATH_TO_CHAR, 'Hit (32x32).png'), MAIN_CHARACTER['SIZE'], (7, 1)),
    'IDLE': load_asset(join(PATH_TO_CHAR, 'Idle (32x32).png'), MAIN_CHARACTER['SIZE'], (11, 1)),
    'JUMP': load_asset(join(PATH_TO_CHAR, 'Jump (32x32).png'), MAIN_CHARACTER['SIZE'], (1, 1)),
    'RUN': load_asset(join(PATH_TO_CHAR, 'Run (32x32).png'), MAIN_CHARACTER['SIZE'], (12, 1)),
    'WALL JUMP': load_asset(join(PATH_TO_CHAR, 'Wall Jump (32x32).png'), MAIN_CHARACTER['SIZE'], (5, 1))
}

# Background tiles
BACKGROUNDS = {
    'BLUE': fill_background(load_asset(join(PATH_TO_BACKGROUND, 'Blue.png'), BACKGROUND['SIZE'], (1,1))),
    'BROWN': fill_background(load_asset(join(PATH_TO_BACKGROUND, 'Brown.png'), BACKGROUND['SIZE'], (1,1))),
    'GRAY': fill_background(load_asset(join(PATH_TO_BACKGROUND, 'Gray.png'), BACKGROUND['SIZE'], (1,1))),
    'GREEN': fill_background(load_asset(join(PATH_TO_BACKGROUND, 'Green.png'), BACKGROUND['SIZE'], (1,1))),
    'PINK': fill_background(load_asset(join(PATH_TO_BACKGROUND, 'Pink.png'), BACKGROUND['SIZE'], (1,1))),
    'PURPLE': fill_background(load_asset(join(PATH_TO_BACKGROUND, 'Purple.png'), BACKGROUND['SIZE'], (1,1))),
    'YELLOW': fill_background(load_asset(join(PATH_TO_BACKGROUND, 'Yellow.png'), BACKGROUND['SIZE'], (1,1))),
}

t = load_asset(join(PATH_TO_TERRAIN,'Terrain (16x16).png'),TERRAIN['SIZE'], (22,11))

TERRAIN = {
    ''
}
