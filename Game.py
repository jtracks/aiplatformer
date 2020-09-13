'''
Runs the main game

Handles the main game logic
'''

import pygame as pg
from Character import Character
from Level import Level
from Config import SCREEN

SCREEN_HEIGHT, SCREEN_WIDTH = SCREEN['SIZE']

def game_loop():
    ''' Main loop for the game engine '''

    screen = pg.display.set_mode(SCREEN['SIZE'])
    pg.display.set_caption("Ai-game")
 
    player = Character()
 
    # Create all the levels
    level_list = [Level(player)]
    current_level_no = 0
    current_level = level_list[current_level_no]
 
    active_sprite_list = pg.sprite.Group()
    player.level = current_level
 
    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT / 4
    active_sprite_list.add(player)
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pg.time.Clock()
 
    # -------- Main Program Loop -----------
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        if (keys := pg.key.get_pressed()):
            if keys[pg.K_LEFT]:
                player.left()
            if keys[pg.K_RIGHT]:
                player.right()
            if keys[pg.K_SPACE]:
                player.jump()
 
            # if event.type == pg.KEYUP:
            #     if event.key == pg.K_LEFT and player.change_x < 0:
            #         player.stop()
            #     if event.key == pg.K_RIGHT and player.change_x > 0:
            #         player.stop()
 
        # Update the player.
        active_sprite_list.update()
 
        # Update items in the level
        current_level.update()
 
        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)
 
        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)
 
        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
 
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
        # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pg.display.flip()


def main():
    ''' Init pg and run game loop '''
    pg.init()

    game_loop()

    pg.quit()

if __name__ == '__main__':
    main()