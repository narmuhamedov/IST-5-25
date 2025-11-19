import pygame
from settings import WIDTH, HEIGHT, FPS
from game.player import Player
from game.fruit import Fruit

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
player = Player()
fruit = Fruit()

all_sprites = pygame.sprite.Group(player, fruit)

score = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()

    # Проверка столкновения
    if pygame.sprite.collide_rect(player, fruit):
        score += 1
        fruit.reset_position()  # Используем метод reset_position вместо fruit.rect.y = 0
    
    screen.fill((0, 50, 100))
    all_sprites.draw(screen)

    text = font.render(f'Счет: {score}', True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()