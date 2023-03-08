import pyautogui as pg
import pygame
import numpy as np
running = True
pygame.init()
mode = 1 #0 for separate values 1 for on same pixel

res = 40
nx, ny = 10, 10
fontsize = res//4
if mode:
    scr = pygame.display.set_mode((res*nx+1,res*ny))
else:
    scr = pygame.display.set_mode((res*nx*2+1,res*ny))
scr.fill((0,0,0))
font=pygame.font.Font('freesansbold.ttf',fontsize)
print_values = False

while running:
    scr.fill((0,0,0))
    cur_pos = pg.position()
    arr = np.array([[(i,j) for i in range(cur_pos[0]-nx//2,cur_pos[0]+nx//2)] for j in range(cur_pos[1]-ny//2,cur_pos[1]+ny//2+1)])

    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
            pygame.quit()
        if eve.type==pygame.KEYDOWN:
            if eve.key == pygame.K_p:
                print_values = True
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            color = pg.pixel(int(arr[i][j][0]),int(arr[i][j][1]))
            if print_values:
                print(color)
            pygame.draw.rect(scr, color, (j*res, i*res, res, res)) #swapped i and j because numpy array is transposed so to make similar to screen
            invert_color = (255-color[0], 255-color[1], 255-color[2])
            R=font.render(str(color[0]),True,(invert_color if mode else (255, 255, 255)))
            G=font.render(str(color[1]),True,(invert_color if mode else (255, 255, 255)))
            B=font.render(str(color[2]),True,(invert_color if mode else (255, 255, 255)))
            scr.blit(R, (((0 if mode else nx)+j)*res, i*res+int(0.5*fontsize)))
            scr.blit(G, (((0 if mode else nx)+j)*res, i*res+int(1.5*fontsize)))
            scr.blit(B, (((0 if mode else nx)+j)*res, i*res+int(2.5*fontsize)))
    if print_values:
        print()
        print_values = False
    pygame.display.update()
