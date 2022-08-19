import pygame

pygame.mixer.init()

bullet_sound = pygame.mixer.Sound('sounds/laser.wav')
alien_shot_sound = pygame.mixer.Sound('sounds/bounce.wav')
theme_song = pygame.mixer.Sound('sounds/alien_invasion.wav')