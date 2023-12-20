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
ButtonFont = pygame.font.SysFont("NeonFont.otf", 75)
Title = TitleFont.render("PythonBets", True, (50,100,148))

#Buttons
GameButton = ButtonFont.render("Games", True, (246,207,67))
WalletButton = ButtonFont.render("Wallet", True, (246,207,67))


#Running variable to check if code should run
screen = "START"

while screen == "START":
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           screen = "END"
        #Title
        pygame.draw.rect(StartScreen, (246,207,67), [175,85,425,100],0)
        StartScreen.blit(Title, (195,100))

        #Games Button
        pygame.draw.rect(StartScreen, (246,207,67), pygame.Rect(240, 295, 300, 60),  2) 
        StartScreen.blit(GameButton, (300,300))

        #Wallet Button
        pygame.draw.rect(StartScreen, (246,207,67), pygame.Rect(240, 400, 300, 60),  2)
        StartScreen.blit(WalletButton, (310,405))
        #Wallet Button
        pygame.display.flip()