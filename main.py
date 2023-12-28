import pygame as pg
from algovis import *
from button import *

pygame.init()

screen_width = 1050
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

done = False
data = random.sample(range(1,2000),1000)
a = Algovis(data,screen,screen_width,screen_height)
main_tick = 60
tick = 1000
start = Button(screen,"start", 45, 80, 10, 5, GREEN,screen_width,screen_height)
stop = pygame.Rect(100, 300, 100, 100)
buttons = [start]
button_color = WHITE
while not done:
    screen.fill(BLACK)
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pg.MOUSEBUTTONUP:
            for button in buttons:
                if button.check_hover(mouse_pos):
                    if button.name == "start":
                        a.vis_quick_sort(tick)






    for button in buttons:
        button.draw()
        if button.check_hover(mouse_pos):
            button.color = RED
        else:
            button.color = WHITE





    pygame.display.flip()


    clock.tick(tick)



