import pygame


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass


    def display(self):
        pygame.display.flip()


    def run(self):
        screen.blit(background, (0, 0))
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)


pygame.init()
pygame.display.set_caption("Starship Engineer")
screen = pygame.display.set_mode((1600, 1080))
background = pygame.image.load("assets/mercury_star_runner.png")

game = Game(screen)
game.run()


class ShipFactory(ABC):
    """
    Factory that represents systems embedded in a starship
    """
    pass


pygame.quit()
print("See you soon Engineer")
