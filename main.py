import pygame
import random

from pygame.sprite import _Group

pygame.init()

# for background
BLUE=pygame.Color("blue")
BLACK=pygame.Color("black")
PINK=pygame.Color("pink")


# for sprite
YELLOW=pygame.Color("yellow")
WHITE=pygame.Color("white")
LIGHT_BLUE=pygame.Color("lightblue")
RED=pygame.Color("red")

# Custom event IDs for color change events
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

class sprite(pygame.sprite.Sprite):
    def __init__(self,color , width , height):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.velocity=[random.choice([-1,1]),random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit=False

        if self.rect.left <= 0 or self.rect.right >= 500:
         self.velocity[0] = -self.velocity[0]
         boundary_hit = True
         
        if self.rect.top <= 0 or self.rect.bottom >= 400:
         self.velocity[1] = -self.velocity[1]
         boundary_hit = True

         if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))
    def change_background_color(self):
       self.image.fill(random.choice([YELLOW,RED,WHITE,LIGHT_BLUE]))    
        