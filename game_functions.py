import pygame
import sys

from bullet import Bullet

def check_events(settings, screen, ship, bullets, map):
    '''Check keyboard and mouse events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, settings, ship, bullets, screen)
        elif event.type == pygame.KEYUP:
            check_keyup(event, settings, ship, bullets, screen)

def check_keydown(event, settings, ship, bullets, screen):
    '''Check events controling ship'''
    if event.key == pygame.K_UP:
        ship.accelerating = True
    elif event.key == pygame.K_DOWN:
        ship.slowing_down = True
    elif event.key == pygame.K_RIGHT:
        ship.rotating_right = True
    elif event.key == pygame.K_LEFT:
        ship.rotating_left = True
    elif event.key == pygame.K_SPACE:
        ship.shooting = True
        
def check_keyup(event, settings, ship, bullets, screen):
    '''Check events controling ship'''
    if event.key == pygame.K_UP:
        ship.accelerating = False
    elif event.key == pygame.K_DOWN:
        ship.slowing_down = False
    elif event.key == pygame.K_RIGHT:
        ship.rotating_right = False
    elif event.key == pygame.K_LEFT:
        ship.rotating_left = False
    elif event.key == pygame.K_SPACE:
        ship.shooting = False


def draw_screen(settings, screen, ship, bullets, enemies):
    '''Draw background and objects to the screen'''
    screen.fill(settings.background)
    for bullet in bullets.sprites():
        bullet.draw()
    ship.draw()
    for enemy in enemies.sprites():
        enemy.draw()
    pygame.display.flip()

def update_objects(ship, bullets, screen, enemies):
    '''Move objects'''
    ship.update()
    ship.shoot(bullets)
    ship.move()
    ship.cooldowns()
    bullets.update()
    enemies.update()

    # Remove bullets that left the screen
    for bullet in bullets.copy():
        if bullet.rect.left > bullet.screen_rect.right or\
          bullet.rect.right < 0 or\
          bullet.rect.top > bullet.screen_rect.bottom or\
          bullet.rect.bottom < 0:
            bullets.remove(bullet)
