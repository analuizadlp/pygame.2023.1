import pygame
import random
from copy import deepcopy
from random import choice, randrange , randint
from config_inicial import largura,altura,mult,tela,fps,quit,start,running, done
from functions import tela_inicio , tela_final, tela_jogo
img_fundo_jogo=pygame.image.load('images/img.png')
img_fundo_jogo = pygame.transform.scale(img_fundo_jogo, (tela ))
pygame.init()
pygame.mixer.init()
fonte=pygame.font.Font('fonte/PressStart2P.ttf', 28)
screen=pygame.display.set_mode(tela)
timer=pygame.time.Clock()
state= start
pygame.mixer.music.load('sons/musica.wav')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops=-1)
while state!= done:
    print(state)
    if state == start:
        state= tela_inicio(screen)
    elif state == running:
        state= tela_jogo(screen)
    else:
        print("entrou yela final")
        state= tela_final(screen)
pygame.quit()
