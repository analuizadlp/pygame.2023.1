import pygame
import random
from copy import deepcopy
from random import choice, randrange , randint
pygame.init()
largura =10
altura=15
mult=40
tela= largura*mult, altura*mult
fps=60
quit=0
start=1
done=66
running=2
img_fundo_jogo= pygame.image.load('images/img.png')
img_fundo_jogo = pygame.transform.scale(img_fundo_jogo, (tela ))
fonte=pygame.font.Font('fonte/PressStart2P.ttf', 28)