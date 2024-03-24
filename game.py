import pygame

from screen import Screen
from grid import Grid

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = Screen((255, 255, 255))
        self.grid = Grid()

        self.menu_on = True
        self.game_on = False

        self.current_player = 'G'

    def run(self):
        while True:
            if self.menu_on:
                self.menu_screen()
            elif self.game_on:
                self.game_screen()
            
            pygame.display.flip()
            self.clock.tick(10)

    def menu_screen(self):
        self.grid.reset_grid()

        self.screen.screen.fill((0, 0, 0))
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
        self.screen.screen.fill((255, 255, 255))
        self.screen.print_text("Game", (0, 0, 0), 0, -470)
        self.screen.print_text("Press ESCAPE for menu screen", (0, 0, 0), 0, -440)

    
        self.grid.print_grid(self.screen.screen)

        if self.grid.check_win('G'):
            self.screen.print_text("WIN GREEN", (0, 255, 0), 0, -410)
            print("Les vert on win")
        elif self.grid.check_win('R'):
            self.screen.print_text("WIN RED", (255, 0, 0), 0, -410)
            print("Les Rouge on win")


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.screen.quit_screen()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Retour au menu")
                    self.menu_on = True
                    self.game_on = False
                    return
                elif pygame.K_KP1 <= event.key <= pygame.K_KP7:  # Vérifie si la touche est entre 1 et 7
                    col = event.key - pygame.K_KP1  # Calcule l'indice de colonne correspondant à la touche numérique
                    print(col + 1)  # Affiche le numéro de colonne
                    if self.grid.place_token(self.current_player, col):
                        self.switch_player()

    def switch_player(self):
        if self.current_player == 'G':
            self.current_player = 'R'
        else:
            self.current_player = 'G'