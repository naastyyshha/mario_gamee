import pygame

from utils import HEIGHT, WIDTH, terminate, FPS


def main_menu(screen):
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры",
                  "Если в правилах несколько строк,",
                  "приходится выводить их построчно"]
    background_img = pygame.transform.scale(pygame.image.load('./data/fon.jpg'), (WIDTH, HEIGHT))
    font_obj = pygame.font.Font(None, 30)
    screen.blit(background_img, (0, 0))
    text_coord = 50
    for line in intro_text:
        string_rendered = font_obj.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type in (pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN):
                return
        pygame.display.update()
        clock.tick(FPS)