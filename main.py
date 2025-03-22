import sys
import pygame
from pygame.locals import *

from nodes import TimeSinceStart
from constants import *

pygame.init()

class GeneratorNodes:

    def __init__(self):

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Generator Nodes")

        self.clock = pygame.time.Clock()
        self.time_delta = 0
        self.fps = 60
        self.nodes = []


    def run(self):

        while True:

            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                    if event.key == K_n:
                        self.add_new_node(0)

                if event.type == MOUSEBUTTONDOWN:
                    for node in self.nodes:
                        node.click(mouse_pos)

                if event.type == MOUSEBUTTONUP:
                    for node in self.nodes:
                        node.unclick(mouse_pos)

            self.screen.fill(Colours.BLACK)

            for node in self.nodes:
                node.process(self.time_delta, mouse_pos)
                node.draw(self.screen, self.time_delta)

            pygame.display.flip()
            self.time_delta = self.clock.tick(self.fps)

    def add_new_node(self, node_selected):
        match node_selected:
            case 0:
                self.nodes.append(TimeSinceStart())


if __name__ == '__main__':

    nodes = GeneratorNodes()
    nodes.run()


