import pygame

from utils import load_image

tile_images = {
    'wall': load_image('box.png'),
    'empty': load_image('grass.png')
}
player_img = load_image('mar.png')

tile_width = tile_height = 100

all_sprite = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
walls = pygame.sprite.Group()
player_group = pygame.sprite.Group()


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, x, y):
        super().__init__(all_sprite, tiles_group)
        self.image = pygame.transform.scale(tile_images.get(tile_type),
                                            (tile_width, tile_height))
        self.rect = self.image.get_rect().move(tile_width * x, tile_height * y)
        if tile_type == 'wall':
            self.add(walls)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprite, player_group)
        self.image = pygame.transform.scale(player_img, (48, 80))
        self.rect = self.image.get_rect().move(tile_width * x + 25, tile_height * y + 5)

    def update(self, event):
        dx, dy = 0, 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                dy = -tile_height
            if event.key == pygame.K_s:
                dy = tile_height
            if event.key == pygame.K_a:
                dx = -tile_width
            if event.key == pygame.K_d:
                dx = tile_width

        self.rect = self.rect.move(dx, dy)
        if pygame.sprite.spritecollide(self, walls, dokill=False):
            self.rect = self.rect.move(-dx, -dy)


def generate_level(level):
    new_player = None
    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell == '#':  # создается стенка
                Tile('wall', x, y)
            elif cell == '.':  # создается дорожка
                Tile('empty', x, y)
            elif cell == '@':  # создается место героя
                Tile('empty', x, y)
                new_player = Player(x, y)
    return new_player
