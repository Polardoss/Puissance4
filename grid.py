import pygame
from config import WIDTH, HEIGHT, W_CELL, H_CELL

class Grid:
    def __init__(self):
        self.grid = [[' ' for _ in range(7)] for _ in range(6)] # Génère une grille 6*7
        self.img_grid = pygame.image.load('img/case.png')
        self.img_grid = pygame.transform.scale(self.img_grid, (W_CELL, H_CELL))
        
        self.img_grid_red = pygame.image.load('img/case_red.png')
        self.img_grid_red = pygame.transform.scale(self.img_grid_red, (W_CELL, H_CELL))

        self.img_grid_green = pygame.image.load('img/case_green.png')
        self.img_grid_green = pygame.transform.scale(self.img_grid_green, (W_CELL, H_CELL))
    
    def print_grid(self, screen):
        for row in range(6):
            for col in range(7):
                x = col * W_CELL
                y = row * H_CELL + 100
                if self.grid[row][col] == ' ':
                    screen.blit(self.img_grid, (x,y))
                elif self.grid[row][col] == 'G':
                    screen.blit(self.img_grid_green, (x,y))
                elif self.grid[row][col] == 'R':
                    screen.blit(self.img_grid_red, (x,y))
    
    def check_column_full(self, col):
        if self.grid[0][col] != ' ': #Colonne full
            print("Colonne Full")
            return True
        return False


    def place_token(self, color, col):
        if self.check_column_full(col): #Colonne full
            return False
        
        for row in range(5, -1, -1):
            if self.grid[row][col] == ' ':
                self.grid[row][col] = color
                return True

