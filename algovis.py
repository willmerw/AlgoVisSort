import pygame
import random
import numpy as np
import math
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.mixer.init()


class Algovis:

    def __init__(self,data,screen,screen_width, screen_height):

        self.screen = screen
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.orig_data = data[:]
        self.data = data
        self.op_time = 1
        self.bar_width = screen_width / len(data)
        self.done = False
        self.sorted = False

        largest_elem = 0
        for elem in data:
            if largest_elem < elem:
                largest_elem = elem
        self.largest_elem = largest_elem

    def vis_insertion_sort(self,tick):
        i = 0
        while not self.done:
            if i == len(self.data)-1:
                self.done = True
            self.screen.fill(BLACK)

            self.check_events()

            self.draw_bars()

            if self.data[i+1] < self.data[i] and i+1 >0:
                self.draw_single_bar(i+1, RED)
                pivot = self.data[i+1]
                self.data[i+1] = self.data[i]
                self.data[i] = pivot
                i = i - 1
            else:
                self.draw_single_bar(i,GREEN)
                i = i + 1

            pygame.display.flip()

            clock.tick(tick)

    def vis_quick_sort(self,tick):
        piv_i = len(self.data) -2

        uncomp_pivs = list(range(0,len(self.data)))
        comp_pivs = []

        i = 0
        i_max = len(self.data)-1
        while not self.done:

            self.play_sound(tick,i)
            piv = self.data[piv_i]
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True

            self.draw_bars()
            self.draw_single_bar(piv_i,RED)
            self.draw_single_bar(i,GREEN)



            if i < piv_i:
                if self.data[i] > piv:
                    elem = self.data[i]
                    self.data.pop(i)
                    self.data.insert(piv_i,elem)
                    piv_i = piv_i - 1
                else:
                    i = i + 1
            elif i == piv_i and i < i_max:
                i = i + 1
            else:
                if self.data[i] < piv:
                    elem = self.data[i]
                    self.data.pop(i)
                    self.data.insert(piv_i, elem)
                    piv_i = piv_i + 1
                else:
                    i = i + 1

            if i == i_max+1:
                comp_pivs.append(piv_i)
                uncomp_pivs.remove(piv_i)
                if len(uncomp_pivs) == 1:
                    self.done = True
                    self.sorted = True
                piv_i = random.sample(uncomp_pivs,1)[0]
                i = 0
                i_max = len(self.data)-1
                for p in comp_pivs:
                    if piv_i < p < i_max:
                        i_max = p
                    if piv_i > p > i:
                        i = p

            pygame.display.flip()

            clock.tick(tick)
        if self.done and self.sorted:
            self.finish(tick)
    def vis_merge_sort(self, tick):
        i = 0
        l_i = 0
        r_i = 0
        parts = []
        new_part = []
        for e in self.data:
            parts.append([e])

        section_complete = False
        j = 0
        k = 0
        while not self.done:
            self.screen.fill(BLACK)
            self.check_events()

            self.draw_bars()

            if not section_complete:
                if parts[j][l_i] > parts[j+1][r_i]:
                    new_part.append(parts[j+1][r_i])
                    r_i += 1
                elif parts[j][l_i] <= parts[j+1][r_i]:
                    new_part.append(parts[j][l_i])
                    l_i += 1

                if r_i >= len(parts[j+1]):
                    new_part = new_part + parts[j][l_i:]
                    section_complete = True

                if l_i >= len(parts[j]):
                    new_part = new_part + parts[j+1][r_i:]
                    section_complete = True

            elif section_complete:
                self.data[i] = new_part[k]
                self.play_sound(tick, i)
                self.draw_single_bar(i, GREEN)
                k += 1
                i += 1
                if k >= len(new_part):

                    parts[j] = new_part
                    parts.pop(j+1)
                    new_part = []
                    k = 0
                    j = j+1
                    l_i = 0
                    r_i = 0
                    section_complete = False

                    if len(parts[0]) == len(self.data):
                        print(len(parts[0]), len(self.data))
                        self.done = True
                        self.sorted = True
            if j+1 >= len(parts):
                j = 0
                i = 0

            pygame.display.flip()

            clock.tick(tick)
        if self.done and self.sorted:
            self.finish(tick)
    def vis_counting_sort(self,tick):
        lowest = float("inf")
        highest = float("-inf")
        for i in self.data:
            if i > highest:
                highest = i
            if i < lowest:
                lowest = i
        r = highest - lowest
        count_ls = []
        aux_ls = []
        for i in range(r+1):
            count_ls.append(0)

        for i in range(len(self.data)):
            aux_ls.append(0)
        i = 0
        counting = True
        sorting = False
        while not self.done:
            self.screen.fill(BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True

            self.draw_bars()

            if counting:
                self.play_sound(tick, i)
                count_ls[self.data[i] - lowest] += 1
                i += 1
                if i > len(self.data)-1:
                    for j in range(1, len(count_ls)):
                        count_ls[j] = count_ls[j]+count_ls[j-1]
                    counting = False
                    sorting = True
                    i = len(self.data) - 1

            elif sorting:
                self.play_sound(tick, i)
                aux_ls[count_ls[self.data[i]-lowest]-1] = self.data[i]
                count_ls[self.data[i]-lowest] -= 1

                i = i - 1
                if i < 0:
                    sorting = False
                    i = len(aux_ls) - 1

            else:
                if i < 0:
                    self.sorted = True
                    self.done = True
                else:
                    self.data[i] = aux_ls[i]
                    self.play_sound(tick, i)
                    i = i - 1
            self.draw_single_bar(i, GREEN)


            pygame.display.flip()

            clock.tick(tick)
        if self.done and self.sorted:
            self.finish(tick)

    def vis_radixmod10_sort(self, tick):

        aux_ls = []
        count_ls = []
        for i in range(10):
            count_ls.append(0)
        for i in range(len(self.data)):
            aux_ls.append(0)
        i = 0
        largest = float("-inf")
        for elem in self.data:
            if elem > largest:
                largest = elem
        k = 0
        while largest % (10**k) < largest:
            k += 1
        j = 1

        counting = True
        sorting = False
        update = False
        while not self.done:
            self.screen.fill(BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
            if counting:
                self.play_sound(tick, i)
                if j <= k:
                    e = self.data[i]
                    print(((e - e % (10 ** (j - 1))) % 10 ** j)//(10**(j-1)))
                    print(count_ls)
                    count_ls[((e - e % (10 ** (j - 1))) % 10 ** j)//(10**(j-1))] += 1
                    i += 1
                    if i == len(self.data):

                        for i in range(1, len(count_ls)):
                            count_ls[i] = count_ls[i] + count_ls[i-1]

                        counting = False
                        sorting = True
                        i = len(self.data) - 1
            elif sorting:
                self.play_sound(tick, i)
                e = self.data[i]

                aux_ls[count_ls[((e - e % (10 ** (j - 1))) % 10 ** j)//(10**(j-1))]-1] = e
                count_ls[((e - e % (10 ** (j - 1))) % 10 ** j)//(10**(j-1))] -= 1
                i = i - 1

                if i < 0 and j <= k:
                    j += 1
                    i = len(self.data) - 1
                    sorting = False
                    update = True
            elif update:

                self.data[i] = aux_ls[i]
                self.play_sound(tick, i)
                i = i - 1
                if i < 0:
                    if j > k:
                        self.done = True
                        self.sorted = True
                    counting = True
                    update = False

                    for i in range(len(count_ls)):
                        count_ls[i] = 0
                        aux_ls[i] = 0
                    i = 0

            self.draw_bars()
            self.draw_single_bar(i,GREEN)


            pygame.display.flip()

            clock.tick(tick)
        if self.done and self.sorted:
            self.finish(tick)

    def get_bar_height(self, e):
        return self.screen_height * (e / self.largest_elem)

    def draw_bars(self):
        for i in range(len(self.data)):
            bar_height = self.get_bar_height(self.data[i])
            bar_rect = (self.bar_width * i, self.screen_height - bar_height, self.bar_width + 1, bar_height)
            pygame.draw.rect(self.screen, WHITE, bar_rect)

    def draw_single_bar(self, i, color):
        bar_height = self.get_bar_height(self.data[i])
        bar_rect = (self.bar_width * i, self.screen_height - bar_height, self.bar_width + 1, bar_height)
        pygame.draw.rect(self.screen, color, bar_rect)

    def play_sound(self, tick, i):
        duration = 1 / tick  # [s]
        sampling_rate = 44100  # default value
        # [Hz]

        frames = int(duration * sampling_rate)
        freq = self.data[i] + 300
        arr = np.cos(2 * np.pi * freq * np.linspace(0, duration, frames))
        sound = np.asarray([32767 * arr, 32767 * arr]).T.astype(np.int16)
        sound = pygame.sndarray.make_sound(sound.copy())
        sound.play()
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:
                    pass

    def finish(self,tick):
        i = 0
        bars = []
        while True:
            self.screen.fill(BLACK)

            self.check_events()

            self.draw_bars()
            for b in bars:
                self.draw_single_bar(b,GREEN)
            if i < len(self.data):
                bars.append(i)
                self.play_sound(tick, i)
                i+=1

            else:
                i = len(self.data)



            pygame.display.flip()

            clock.tick(tick)


    pygame.quit()


