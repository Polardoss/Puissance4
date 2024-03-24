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
    

    def reset_grid(self):
        self.grid = [[' ' for _ in range(7)] for _ in range(6)]


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
    
    def check_win(self, color):
        if self.check_row(color):
            return True
        elif self.check_col(color):
            return True
        elif self.check_diagonal(color):
            return True
        return False
        

    def check_row(self, color):
        for row in self.grid: #Check line
            count = 0
            for cell in row:
                if cell == color:
                    count +=1
                    if count == 4: 
                        return True
                else: 
                    count = 0
        return False
    

    def check_col(self, color):
        for col in range(len(self.grid[0])): #Check column
            count = 0
            for row in self.grid:
                if row[col] == color:
                    count +=1
                    if count == 4: 
                        return True
                else: 
                    count = 0
        return False
    
    def check_diagonal(self, color):
        for i in range(len(self.grid) - 3):  # Parcours des lignes
            for j in range(len(self.grid[0]) - 3):  # Parcours des colonnes
                # Vérification de la diagonale de gauche à droite (\)
                if (self.grid[i][j] == color and
                    self.grid[i+1][j+1] == color and
                    self.grid[i+2][j+2] == color and
                    self.grid[i+3][j+3] == color):
                    return True
                # Vérification de la diagonale de droite à gauche (/)
                if (self.grid[i][j+3] == color and
                    self.grid[i+1][j+2] == color and
                    self.grid[i+2][j+1] == color and
                    self.grid[i+3][j] == color):
                    return True
        return False

                


