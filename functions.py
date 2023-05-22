import pygame
import random
from copy import deepcopy
from random import choice, randrange , randint
from config_inicial import largura,altura,mult,tela,fps,quit,start,running, img_fundo_jogo

def tela_inicio(screen):
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    fundo = pygame.image.load('images/img_fim.png')
    fundo=pygame.transform.scale(fundo,(tela))

    roda = True
    while roda:

        # Ajusta a velocidade do jogo.
        clock.tick(fps)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = quit
                roda = False

            if event.type == pygame.KEYUP:
                state = running
                roda = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill((0,0,0))
        screen.blit(fundo, (0,0))

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    return state
