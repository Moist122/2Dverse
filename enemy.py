import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    '''Abstract class representing any enemy.'''
    def __init__(self):
        super().__init__()
        self.contact_damage = 5