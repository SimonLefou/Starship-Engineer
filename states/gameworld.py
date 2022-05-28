import pygame
import os
from states.state import State


class GameWorld(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.bg_img = pygame.image.load(
            os.path.join(self.game.assets_dir, "ship", "1200px-Port_Olisar_far_away-1455658027.png"))

    def update(self, delta_time, actions):
        pass

    def render(self, display):
        display.blit(self.bg_img, (0, 0))


class Player:
    pass

