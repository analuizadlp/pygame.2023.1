import pygame
import random
from copy import deepcopy
from random import choice, randrange , randint
from config_inicial import largura,altura,mult,tela,fps,quit,start,running, done,img_fundo_jogo, fonte

# Inserção da tela inicial
def tela_inicio(screen):
    clock = pygame.time.Clock()

    # Carrega imagem
    fundo = pygame.image.load('images/Tela inicial.jpg')
    # Ajusta a escala 
    fundo=pygame.transform.scale(fundo,(tela))

    # Determina comandos da tela inicial
    roda = True
    while roda:
        # Ajusta a velocidade do jogo.
        clock.tick(fps)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Aplica comando para sair do jogo
            if event.type == pygame.QUIT:
                state = done
                roda = False

        # Aplica comando para iniciar o jogo (ir para próxima tela)
            if event.type == pygame.KEYUP:
                state = running
                roda = False

        # A cada loop, preenche o fundo com a imagem da tela inicial
        screen.fill((255,0,0))
        screen.blit(fundo, (0,0))

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    return state

# Inserção da tela final
def tela_final(screen):
    timer=pygame.time.Clock()

    # Carrega imagem
    fundo2 = pygame.image.load('images/Tela final.jpg')
    # Ajusta escala 
    fundo2=pygame.transform.scale(fundo2,(tela))

    # Determina comandos da tela final
    roda= True
    while roda:
        timer.tick(fps)
        for event in pygame.event.get():
            # Comando para sair do jogo 
            if event.type == pygame.QUIT:
                state = done
                roda=False
            # Comando para pressionar "S" e sair do jogo
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    state = done
                    roda=False
            # Comando para pressionar "espaço" e recomeçar o jogo
                if event.key == pygame.K_SPACE:
                    state= running
                    roda=False

            # A cada loop, preenche o fundo com a imagem da tela inicial
            screen.fill((0,0,0))
            screen.blit(fundo2, (0,0))

            # Depois de desenhar tudo, inverte o display.
            pygame.display.flip()

    return state
    
# Inserção da tela do jogo
def tela_jogo(screen):
    # Formação dos blocos 
    cores = [(255,0, 0) ,(0,255, 0), (0,0, 255),(255,233, 0)]
    rnumero = randint(0,3)
    grid= [pygame.Rect(x*mult,y*mult,mult,mult)  for x in range(largura) for y in range(altura)]
    # Lista de coordenadas dos blocos
    blocos_ini=[[(-1,0),(-2,0),(0,0),(1,0)],
            [(0,-1),(-1,-1),(-1,0),(0,0)],
            [(-1,0),(-1,1),(0,0),(0,-1)],
            [(0,0),(-1,0),(0,1),(-1,-1)],
            [(0,0),(0,-1),(0,1),(-1,-1)],
            [(0,0),(0,-1),(0,1),(-1,-1)],
            [(0,0),(0,-1),(0,1),(-1,0)]]
    # Criação dos blocos
    blocos = []
    for bl in blocos_ini:
        rect_list = []
        for x, y in bl:
            rect = pygame.Rect(x + largura // 2, y + 1, 1, 1)
            rect_list.append(rect)
        blocos.append(rect_list)
    bloco_rect=pygame.Rect(0,0,mult-2,mult-2)
    field=[[0 for i in range(largura)]for j in range(altura)]

    # Parâmetros para a animação dos blocos 
    anima_conta=0
    anima_limite=2000
    anima_vel=30
    bloco=deepcopy(choice(blocos))

    # Delimitação das bordas 
    def borders():
        if bloco[i].x<0 or bloco[i].x> largura-1:
            return False
        elif bloco[i].y>altura-1 or field[bloco[i].y][bloco[i].x]:
            return False
        return True
    
    # Contagem dos pontos 
    score=0
    linhascoletadas=0
    # Determinação do loop do jogo
    roda= True
    while roda:
        vel_x,rotate=0,False
        screen.fill(pygame.Color('White'))
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                exit()
            # Movimentacao do bloco - atribuição de velocidade
            if event.type==pygame.KEYDOWN:
                if event.key== pygame.K_LEFT:
                    vel_x= -1
                elif event.key== pygame.K_RIGHT:
                    vel_x= 1
                elif event.key==pygame.K_DOWN:
                    anima_limite=100
                elif event.key==pygame.K_UP:
                    rotate= True
        
        # Preenche o bloco fixado com a cor branca
        screen.fill((0, 0, 0)) 
        screen.blit(img_fundo_jogo, (0, 0))

        # Move bloco (eixo x) - Aplicação da velocidade
        old_bloc=deepcopy(bloco)
        for i in range(4):
            bloco[i].x+= vel_x
            if not borders():
                bloco=deepcopy(old_bloc)
                break
        # Move bloco (eixo y) - Aplicação da velocidade
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

        # Rotação do bloco
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

        # Checa as linhas e marca os pontos (score)
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
        # Determina que se os blocos chegarem ao limite de altur, o jogo acaba
        if altura_linhas >= 14:
            roda= False  
        
        # Escreve os pontos (score)
        text_surface = fonte.render("{:08d}".format(score), True, (255, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (largura / 2,  10)
        screen.blit(text_surface, text_rect)

        # Insere os blocos
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
    state = quit
    return state
        

            
            
