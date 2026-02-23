import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height, is_ai=False):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.rect = self.image.get_rect()
        self.speed = 5
        self.is_ai = is_ai
        
    def moveUp(self, pixels):
        self.rect.y -= pixels
        # Check that you are not going too far (off screen)
        if self.rect.y < 0:
            self.rect.y = 0
          
    def moveDown(self, pixels, screen_height):
        self.rect.y += pixels
        # Check that you are not going too far (off screen)
        if self.rect.y > screen_height - self.rect.height:
            self.rect.y = screen_height - self.rect.height

    def update_ai(self, ball, screen_height):
        if self.is_ai:
            if self.rect.centery < ball.rect.centery:
                self.moveDown(self.speed, screen_height)
            if self.rect.centery > ball.rect.centery:
                self.moveUp(self.speed)

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.velocity = [random.randint(4, 8), random.randint(-8, 8)]
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = random.randint(-8, 8)
