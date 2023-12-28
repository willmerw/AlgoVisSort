import pygame as pg
import pygame.draw


class Button:
    def __init__(self,screen, name,  x, y, width, height, color, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = int(screen_width * (x/100))
        self.y = int(screen_height * (y/100))
        self.width = int(screen_width * (width/100))
        self.height = int(screen_width * (height/100))
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.color = color
        self.name = name

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def check_hover(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)