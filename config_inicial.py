# Importações 
import pygame
import random
from copy import deepcopy
from random import choice, randrange , randint
pygame.init()
# Determinação de parâmetros
largura =10
altura=15
mult=40
tela= largura*mult, altura*mult
fps=30
quit=0
start=1
done=3
running=2
# Download das imagens 
img_fundo_jogo= pygame.image.load('images/img.png')
img_fundo_jogo = pygame.transform.scale(img_fundo_jogo, (tela ))
fonte=pygame.font.Font('fonte/PressStart2P.ttf', 28)