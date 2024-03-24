import pygame
from config import WIDTH, HEIGHT

class Screen:
    def __init__(self, color):
        self.text_font = pygame.font.SysFont("monospace", 20) #Police d'écriture
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.screen.fill(color)
        pygame.display.set_caption("Puissance 4")

    def quit_screen(self):
        print("Fermeture screen")
        pygame.quit()
        quit()

    def print_text(self, text, color, gap_x=0, gap_y=0): # X = Largeur   Y = hauteur
        text_surface = self.text_font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(self.screen.get_width() // 2 + gap_x, self.screen.get_height() // 2 + gap_y))
        self.screen.blit(text_surface, text_rect)
