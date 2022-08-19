import pygame
from random import choice

pygame.mixer.init()

theme_song = pygame.mixer.Sound('sounds/alien_invasion.wav')

bullet_sounds = [
    pygame.mixer.Sound('sounds/laser1.wav'),
    pygame.mixer.Sound('sounds/laser2.wav'),
    pygame.mixer.Sound('sounds/laser3.wav'),
]

alien_shot_sound = pygame.mixer.Sound('sounds/bounce.wav')
create_fleet_sound = pygame.mixer.Sound('sounds/create_fleet.wav')
ship_hit_sound = pygame.mixer.Sound('sounds/ship_hit.wav')