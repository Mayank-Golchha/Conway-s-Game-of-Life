# RULE 1 : A live cell with fewer than two live neighbours dies (underpopulation)
# RULE 2 : A live cell with two or three live neighbours remains alive (survival)
# RULE 3 : A live cell with more than three live neighbours dies (overpopulation)
# RULE 4 : A dead cell with exactly three live neighbours become alive (reproduction)

# in grid
# 0 for dead cell
# 1 for live cell
import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import pygame
import copy


pygame.init()
length = 900
grid = [[0 for i in range(length)] for j in range(length)] # to store next state
temp_grid = copy.deepcopy(grid) # to store prev state

screen = pygame.display.set_mode((length, length), pygame.RESIZABLE)
cell_size = 15
width = int(length/cell_size)
cells = []

def condition(x,y):
    neighbours = [[x+1,y],[x,y+1],[x+1,y+1],[x-1,y],[x,y-1],[x-1,y-1],[x-1,y+1],[x+1,y-1]]
    neighbours = [temp_grid[i[1]][i[0]] for i in neighbours if i[0] < width and i[1] < width and i[0] >= 0 and i[1] >= 0]
    live_cells = 0
    cell = temp_grid[y][x]
    for i in neighbours:
        if i:
            live_cells += 1

    if cell:
        if live_cells < 2:
            grid[y][x] = 0 # rule 1
        elif live_cells == 2 or live_cells == 3:
            pass # rule 2
        elif live_cells > 3:
            grid[y][x] = 0 # rule 3
    elif not cell and live_cells == 3:
        grid[y][x] = 1 # rule 4

def drawSquare(x,y):
    pygame.draw.rect(screen, "black", (x * cell_size, y * cell_size, cell_size-1, cell_size-1))


def draw_grid():
    for x in range(0,length,cell_size):
        pygame.draw.line(screen,"black",(x,0),(x,length),width=1)

    for y in range(0,length,cell_size):
        pygame.draw.line(screen,"black",(0,y),(length,y),width=1)

    for y in range(width):
        for x in range(width):
            if grid[y][x]:
                drawSquare(x,y)

def cell_condition():
    [condition(x,y) for y in range(width) for x in range(width)]


running = True

clock = pygame.time.Clock()
hold = 0 # if shift key is pressed cells condition will not change

while running:
    screen.fill("white")
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            x = int(x/cell_size)
            y = int(y/cell_size)
            # if not grid[y][x]:
            grid[y][x] ^= 1
        elif event.type == pygame.KEYDOWN:
            # when shift is pressed and if hold is 0
            # then cells condition will not change and you can put more cells with mouse clicks
            # press shift again to start life
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                hold ^= 1

    draw_grid()
    if not hold:
        temp_grid = copy.deepcopy(grid)
        cell_condition()

    pygame.display.flip()

pygame.quit()

