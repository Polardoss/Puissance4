import pygame
import random

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

        self.alone_mode = None

        self.current_player = 'G'
        self.current_player_is_ia = True

        self.winner = ' '

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
        self.winner = ' '

        self.screen.screen.fill((0, 0, 0))
        self.screen.print_text("Menu", (255, 255, 255), 0, -470)
        self.screen.print_text("Press SPACE for play Alone", (255, 255, 255), 0, -440)
        self.screen.print_text("Press TAB to play with others", (255, 255, 255), 0, -410)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.screen.quit_screen()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Lancement du jeu SEUL")
                    self.alone_mode = True
                    self.menu_on = False
                    self.game_on = True
                    return
                elif event.key == pygame.K_TAB:
                    print("Lancement du jeu SEUL")
                    self.alone_mode = False
                    self.menu_on = False
                    self.game_on = True
                    return

    def game_screen(self):
    
        if self.alone_mode:
            self.screen.print_text("Alone Mode", (0, 0, 0), 0, -470)
            self.mode_alone() #Mode seul 
        else:
            self.screen.print_text("Multiplayer Mode", (0, 0, 0), 0, -470)
            self.mode_multiplayer()


        if self.grid.check_win('G'):
            self.screen.print_text("WIN GREEN", (0, 255, 0), 0, -410)
            print("Les vert on win")
            self.winner = 'G'
        elif self.grid.check_win('R'):
            self.screen.print_text("WIN RED", (255, 0, 0), 0, -410)
            print("Les Rouge on win")
            self.winner = 'R'

        
        

    def switch_player(self):
        if self.current_player_is_ia:
            self.current_player_is_ia = False
        else:
            self.current_player_is_ia = True

        if self.current_player == 'G':
            self.current_player = 'R'
        else:
            self.current_player = 'G'

    def mode_multiplayer(self):
        
        if self.current_player == 'G':
            self.screen.screen.fill((0, 255, 0))
        else:
            self.screen.screen.fill((255, 0, 0))
        print(f"C'est le tour de {self.current_player}")
        self.screen.print_text("Press ESCAPE for menu screen", (0, 0, 0), 0, -440)
        self.grid.print_grid(self.screen.screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.screen.quit_screen()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Retour au menu")
                    self.menu_on = True
                    self.game_on = False
                    return
                elif pygame.K_KP1 <= event.key <= pygame.K_KP7 and self.winner == ' ':  # Vérifie si la touche est entre 1 et 7
                    col = event.key - pygame.K_KP1  # Calcule l'indice de colonne correspondant à la touche numérique
                    print(col + 1)  # Affiche le numéro de colonne
                    if self.grid.place_token(self.current_player, col):
                        self.switch_player()
                    else:
                        print("Impossible de placer le jeton")

    def mode_alone(self):
        if self.current_player == 'G':
            self.screen.screen.fill((0, 255, 0))
        else:
            self.screen.screen.fill((255, 0, 0))
        print(f"C'est le tour de {self.current_player}")
        self.screen.print_text("Press ESCAPE for menu screen", (0, 0, 0), 0, -440)
        self.grid.print_grid(self.screen.screen)

        if self.current_player_is_ia:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.screen.quit_screen()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        print("Retour au menu")
                        self.menu_on = True
                        self.game_on = False
                        return
                    
            #L'IA JOUE
            if not self.grid.check_win('G') and not self.grid.check_win('R'):  # Vérifie si personne n'a gagné encore
                col =random.randint(0,6)
                if self.grid.place_token(self.current_player, col):
                    self.switch_player()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.screen.quit_screen()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        print("Retour au menu")
                        self.menu_on = True
                        self.game_on = False
                        return
                    elif pygame.K_KP1 <= event.key <= pygame.K_KP7 and self.winner == ' ':  # Vérifie si la touche est entre 1 et 7
                        col = event.key - pygame.K_KP1  # Calcule l'indice de colonne correspondant à la touche numérique
                        print(col + 1)  # Affiche le numéro de colonne
                        if self.grid.place_token(self.current_player, col):
                            self.switch_player()
                        else:
                            print("Impossible de placer le jeton")
        