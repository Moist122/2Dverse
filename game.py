import pygame
from pygame.sprite import Group

from vector import Vector

from settings import Settings
from ship import Ship
import game_functions as gf
from bullet import Bullet
from mine import Mine

def run_game():
    # Initialize pygame and screen
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("2Dverse")

    # Create ship and groups for bullets, enemies and obstacles
    ship = Ship(screen)
    bullets = Group()
    enemies = Group()
    obstacles = Group()
    mine = Mine(screen, Vector(40, 40))

    # Main game loop
    while True:

        gf.check_events(settings, screen, ship, bullets)
        gf.update_objects(ship, bullets, screen, mine)
        gf.draw_screen(settings, screen, ship, bullets, mine)

run_game()