import pygame
from algovis import *

pygame.init()

screen_width = 650
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

# Loop until the user clicks the close button.
done = False
data = random.sample(range(1,100000000),1000)
print(data)
a = Algovis(data,screen,screen_width,screen_height)

a.vis_radixmod10_sort(1000)

