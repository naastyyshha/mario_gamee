import pygame

from menu import main_menu
from sprites import generate_level, tiles_group, player_group, all_sprite
from utils import terminate, SCREEN_SIZE, FPS, load_level, Camera

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)


def game():
    game_level = load_level('map.txt')

    player = generate_level(game_level)

    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            player.update(event)

        camera = Camera()
        clock = pygame.time.Clock()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                player.update(event)
            screen.fill('black')

            camera.update(player)

            for sprite in all_sprite:
                camera.apply(sprite)

            tiles_group.draw(screen)
            player_group.draw(screen)

            pygame.display.update()
            clock.tick(FPS)


clock = pygame.time.Clock()
run = True
while run:
    main_menu(screen)
    game()
