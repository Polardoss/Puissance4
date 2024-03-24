import pygame

from screen import Screen
from grid import Grid

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = Screen((255, 255, 255))

        self.menu_on = True
        self.game_on = False

    def run(self):
        while True:
            if self.menu_on:
                self.menu_screen()
            elif self.game_on:
                self.game_screen()
            
            pygame.display.flip()
            self.clock.tick(10)

    def menu_screen(self):
        self.screen = Screen((0, 0, 0))
        self.screen.print_text("Menu", (255, 255, 255), 0, -470)
        self.screen.print_text("Press SPACE for play", (255, 255, 255), 0, -440)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.screen.quit_screen()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Lancement du jeux")
                    self.menu_on = False
                    self.game_on = True
                    return

    def game_screen(self):
        self.screen = Screen((255, 255, 255))
        self.screen.print_text("Game", (0, 0, 0), 0, -470)
        self.screen.print_text("Press ESCAPE for menu screen", (0, 0, 0), 0, -440)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.screen.quit_screen()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Retour au menu")
                    self.menu_on = True
                    self.game_on = False
                    return