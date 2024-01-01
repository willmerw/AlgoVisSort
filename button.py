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
        self.font_size = self.height // 2
        self.font = pygame.font.SysFont("consolas", self.font_size, bold = True)
        self.text = self.font.render(self.name, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.x + (self.width//2), self.y + (self.height//2))

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.text, self.text_rect)

    def check_hover(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)