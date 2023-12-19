import pygame
from pygame.locals import *

#Initialize
pygame.init()
pygame.font.init()

#Variables
background_colour = (0,0,0)


#Start Screen
StartScreen = pygame.display.set_mode((750,750))
StartScreen.fill(background_colour)
pygame.display.set_caption('PythonBets')
pygame.display.flip()

#Font
TitleFont = pygame.font.SysFont("NeonFont.otf", 100)
Title = TitleFont.render("PythonBets", True, (50,104,148))


#Running variable to check if code should run
screen = "START"

while screen == "START":
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           screen = "END"
        
        pygame.draw.rect(StartScreen, (246,207,67), [180,85,425,100],0)
        StartScreen.blit(Title, (200,100))
        pygame.display.flip()