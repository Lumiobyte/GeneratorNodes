import pygame
from pygame.locals import *
from constants import *

def clamp(num, lower, upper):
    return max(lower, min(num, upper))

class Node:
    def __init__(self, name, connections):
        self.name = name
        self.connections = connections
        self.rect = pygame.Rect(0, 0, 200, 100 + 50 * len(connections))
        self.pos = (500, 500)
        self.font = pygame.font.SysFont("Arial", 12)

        self.grabbed = False
        self.grab_offset = (0, 0)

    def click(self, mouse_pos):

        collision_rect = pygame.Rect(self.rect.left + self.pos[0], self.rect.top + self.pos[1], self.rect.width, self.rect.height)

        if not self.grabbed and collision_rect.collidepoint(mouse_pos):

            connection_grabbed = False
            for connection in self.connections:
                if connection.check(mouse_pos):
                    connection_grabbed = True
                    # If connection is colliding, start dragging a line

            if not connection_grabbed:
                self.grabbed = True
                self.grab_offset = (mouse_pos[0] - self.pos[0], mouse_pos[1] - self.pos[1])

    def unclick(self, mouse_pos):
        self.grabbed = False

    def process(self, time_delta, mouse_pos):

        if self.grabbed:
            self.pos = (clamp(mouse_pos[0] - self.grab_offset[0], 0, WIDTH - self.rect.width), clamp(mouse_pos[1] - self.grab_offset[1], 0, HEIGHT - self.rect.height))

    def draw(self, surface, time_delta):

        outline_colour = Colours.OUTLINE_GRAY
        if self.grabbed: # Selection outline
            outline_colour = Colours.CREAM
        scaled_rect = self.rect.inflate(8, 8)
        pygame.draw.rect(surface, outline_colour, pygame.Rect(scaled_rect.left + self.pos[0], scaled_rect.top + self.pos[1], scaled_rect.width, scaled_rect.height))

        pygame.draw.rect(surface, Colours.GRAY, pygame.Rect(self.rect.left + self.pos[0], self.rect.top + self.pos[1], self.rect.width, self.rect.height))

        surface.blit(self.font.render(self.name, True, Colours.WHITE), (self.pos[0] + 10, self.pos[1] + 10))


class TimeSinceStart(Node):
    def __init__(self):
        super().__init__("Time Since Start", [])

    def process(self, time_delta, mouse_pos):
        super().process(time_delta, mouse_pos)