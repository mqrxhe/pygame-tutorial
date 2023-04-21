import pygame, sys

CLK = pygame.time.Clock()

from pygame.locals import *
pygame.init() # initiates pygame

pygame.display.set_caption("My game!")

WINDOW_SIZE = (400,400)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32) # initiates window

while True:

    # Iterates through all events; an event is any button or key press
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    CLK.tick(60) # framerate = 60
