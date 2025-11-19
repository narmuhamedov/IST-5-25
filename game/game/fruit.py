import pygame
from settings import HEIGHT, WIDTH, FRUIT_SPEED
import random

class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.reset_position()
    
    def reset_position(self):
        # Сбрасываем позицию как по X, так и по Y
        self.rect.x = random.randint(0, WIDTH - 20)
        self.rect.y = 0
    
    def update(self):
        self.rect.y += FRUIT_SPEED
        if self.rect.y > HEIGHT:  # Лучше использовать HEIGHT вместо 400
            self.reset_position()