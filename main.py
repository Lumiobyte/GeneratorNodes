import pygame
from pygame.locals import *

screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Generator Nodes")

fps = 60
clock = pygame.time.Clock()

nodes = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_n:
                pass  # Create new node
