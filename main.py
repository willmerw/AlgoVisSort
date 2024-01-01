import pygame as pg
from algovis import *
from button import *

pygame.init()

screen_width = 1050
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

done = False
data = random.sample(range(1,2000),1000)
a = Algovis(data,screen,screen_width,screen_height)
main_tick = 60
tick = 1000
start = Button(screen, "Start", 45, 80, 10, 5, WHITE, screen_width, screen_height)
#stop = Button(screen, "Stop", 30, 10, 20, 30, WHITE, screen_width, screen_height)
buttons = [start]
button_color = WHITE


title_font = pygame.font.SysFont("consolas", screen_height // 10, bold = True)
title_text = title_font.render("Algo Vis", True, GREEN)
title_rect = title_text.get_rect()
title_rect.center = (screen_width // 2, (screen_height // 10) // 2 + 10)

sub_title_font = pygame.font.SysFont("consolas", screen_height//30, bold = True)
sub_title_text = sub_title_font.render("Sorting Edition", True, GREEN)
sub_title_rect = sub_title_text.get_rect()
sub_title_rect.center = (screen_width // 2, title_rect.y + title_text.get_height() + 10)

d_time = 0
tot_time = 0
rot = 0
while not done:
    screen.fill(BLACK)
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pg.MOUSEBUTTONUP:
            for button in buttons:
                if button.check_hover(mouse_pos):
                    if button.name == "Start":
                        a.vis_quick_sort(tick)






    for button in buttons:
        button.draw()
        if button.check_hover(mouse_pos):
            button.color = GREEN
        else:
            button.color = WHITE


    screen.blit(title_text, title_rect)
    screen.blit(sub_title_text,sub_title_rect)

    d_time = d_time + clock.get_time()

    if d_time >= 60:
        rot += math.pi/8
        title_rect = title_rect.move(0, int(2 * math.sin(rot)))
        sub_title_rect = sub_title_rect.move(0, int(2 * math.sin(rot)))

        d_time = 0


    pygame.display.flip()


    clock.tick(tick)



