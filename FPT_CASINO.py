import pygame
from pygame.locals import *

#Variables
background_colour = (255,255,255)

#Start Screen
StartScreen = pygame.display.set_mode((750,750))
StartScreen.fill(background_colour)
pygame.display.set_caption('PythonBets')
pygame.display.flip()

#Running variable to check if code should run
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False