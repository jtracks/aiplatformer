'''
Character
--------------

Contains the CharacterBot class with is a Character but controlled by the cpu.

'''
import pygame as pg
import numpy as np
from Character import Character
from random import randint
from Config import MAIN_CHARACTER
from functools import lru_cache

class CharacterBot(Character):
    ''' A character controller by the cpu.

    Extension of :class: `pg.sprite.Sprite` and :class: `Character`.

    :param name: Indentifier for character, defaults to 'Player 1'
    :type name: str, optional

    :param character: Name of assets for textures, defaults to 'Ninja frog'
    :type character: str, optional

    '''

    width, height = MAIN_CHARACTER['SIZE'] 
    speed_x , speed_y = (0, 0)
    level = None
    tick = 1
    state = 'IDLE' # ['DOUBLE JUMP', 'FALL', 'HIT', 'IDLE', 'JUMP', 'RUN', 'WALL JUMP']
    state_img = 0
    direction = 'RIGHT' #['LEFT', 'RIGHT']
    double_jump = True

    def __init__(self, name='Bot1', character='Ninja frog'):
        super(CharacterBot, self).__init__(name, character)

    def _tint_image(self):
        ''' Add a colored tint to image in order to make it destinct '''
        tint_color = self._get_tint()
        self.image = self.image.copy()
        self.image.fill(tint_color, None, pg.BLEND_RGBA_MULT)

    @lru_cache(maxsize=None)
    def _get_tint(self):
        ''' Returns a random color to tint the character in.

        :return: Color
        :rtype: (int, int, int)

        '''
        return (randint(0,255), randint(0,255), randint(0,255))

    def random_action(self):
        ''' Do a random action '''
        actions = np.random.choice([[self.jump], [self.jump, self.right], [self.jump, self.left], [self.right], [self.left]],
            1,
            [0.03, 0.06, 0.01, 0.70, 0.20]
            )
        for action in actions[0]:
            action()

