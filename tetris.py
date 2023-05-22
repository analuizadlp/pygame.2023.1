import pygame
import random
from copy import deepcopy
from random import choice, randrange , randint
from config_inicial import largura,altura,mult,tela,fps,quit,start,running
from functions import tela_inicio
img_fundo_jogo=pygame.image.load('images/img.png')
img_fundo_jogo = pygame.transform.scale(img_fundo_jogo, (tela ))
pygame.init()
fonte=pygame.font.Font('fonte/PressStart2P.ttf', 28)
screen=pygame.display.set_mode(tela)
timer=pygame.time.Clock()
cores=[(255,0, 0) ,(0,255, 0), (0,0, 255),(255,233, 0) ]
rnumero=randint(0,3)
grid= [pygame.Rect(x*mult,y*mult,mult,mult)  for x in range(largura) for y in range(altura)]
blocos_ini=[[(-1,0),(-2,0),(0,0),(1,0)],
            [(0,-1),(-1,-1),(-1,0),(0,0)],
            [(-1,0),(-1,1),(0,0),(0,-1)],
            [(0,0),(-1,0),(0,1),(-1,-1)],
            [(0,0),(0,-1),(0,1),(-1,-1)],
            [(0,0),(0,-1),(0,1),(-1,-1)],
            [(0,0),(0,-1),(0,1),(-1,0)]]
blocos = []
for bl in blocos_ini:
    rect_list = []
    for x, y in bl:
        rect = pygame.Rect(x + largura // 2, y + 1, 1, 1)
        rect_list.append(rect)
    blocos.append(rect_list)
bloco_rect=pygame.Rect(0,0,mult-2,mult-2)
field=[[0 for i in range(largura)]for j in range(altura)]


anima_conta=0
anima_limite=2000
anima_vel=60

bloco=deepcopy(choice(blocos))
def borders():
    if bloco[i].x<0 or bloco[i].x> largura-1:
        return False
    elif bloco[i].y>altura-1 or field[bloco[i].y][bloco[i].x]:
        return False
    return True
score=0
linhascoletadas=0
state= tela_inicio(screen)
while state==running:
    vel_x,rotate=0,False
    screen.fill(pygame.Color('White'))
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key== pygame.K_LEFT:
                vel_x= -1
            elif event.key== pygame.K_RIGHT:
                vel_x= 1
            elif event.key==pygame.K_DOWN:
                anima_limite=100
            elif event.key==pygame.K_UP:
                rotate= True
    
    screen.fill((0, 0, 0))  # Preenche com a cor branca
    screen.blit(img_fundo_jogo, (0, 0))
    #move x 
    old_bloc=deepcopy(bloco)
    for i in range(4):
        bloco[i].x+= vel_x
        if not borders():
            bloco=deepcopy(old_bloc)
            break
    #move y
    anima_conta+=anima_vel
    if anima_conta>=anima_limite:
        anima_conta=0
        old_bloc=deepcopy(bloco)
        for i in range(4):
            bloco[i].y+= 1
            if not borders():
                for i in range(4):
                    field[old_bloc[i].y][old_bloc[i].x]=cores[rnumero]
                bloco=deepcopy(choice(blocos))
                anima_limite=2000
                break
    #rotate
    center=bloco[0]
    old_bloc=deepcopy(bloco)
    if rotate:
        for i in range(4):
            x=bloco[i].y - center.y
            y=bloco[i].x - center.x
            bloco[i].x= center.x-x
            bloco[i].y= center.y+y
            if not borders():
                bloco=deepcopy(old_bloc)
                break
    #check lines
    line= altura-1
    coletadas=0
    n_coletadas=0
    altura_linhas=0
    for row in range(altura-1,-1,-1):
        count=0
        for i in range(largura):
            if field[row][i]:
                count+=1
            field[line][i]= field[row][i]
        if count<largura:
            line-=1
            n_coletadas+=1
        else: 
            score+=100
    altura_linhas=0
    densidade=0
    for vertical in range(altura):
        for horizontal in range(largura):
            if field[vertical][horizontal]!=0:
                altura_linhas+=1
                break   
    if altura_linhas >= 14:
        running = False    
    #check if the game is over
    
    
    text_surface = fonte.render("{:08d}".format(score), True, (255, 255, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (largura / 2,  10)
    screen.blit(text_surface, text_rect)


    

    [pygame.draw.rect(screen,(40,40,40),i_rect,1)for i_rect in grid]
    for i in range(4):
        bloco_rect.x= bloco[i].x*mult
        bloco_rect.y= bloco[i].y*mult
        pygame.draw.rect(screen,cores[rnumero],bloco_rect)
    for y, raw in enumerate(field):
        for x,col in enumerate(raw):
            if col:
                bloco_rect.x, bloco_rect.y=x*mult,y *mult
                pygame.draw.rect(screen,col,bloco_rect)
    rnumero=randint(0,2)
    
    pygame.display.flip()
    timer.tick(fps)