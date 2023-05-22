import pygame
import random
from copy import deepcopy
from random import choice, randrange , randint

largura =10
altura=15
mult=40
tela= largura*mult, altura*mult
fps=60
quit=0
start=1
running=2
img_fundo_jogo= pygame.image.load('images/img.png')
img_fundo_jogo = pygame.transform.scale(img_fundo_jogo, (tela ))
