import pygame
from pygame.locals import *
from sys import exit
from random import randint


pygame.init()
# Variaveis
largura = 640
altura = 480
x_cobra = largura/2
y_cobra = altura/2
x_maca= randint(40,600)
y_maca = randint(50,450)
pontos = 0
fonte = pygame.font.SysFont('arial',40, True, True)
tela = pygame.display.set_mode((largura, altura))
pygame.mixer_music.set_volume(0.2)
fundo = pygame.mixer_music.load('SUPER MARIO BROS MÚSICAS.mp3')
pygame.mixer_music.play(-1)
colisao = pygame.mixer.Sound('smw_kick.wav')
pygame.display.set_caption('JOGO DA COBRINHA')
relogio = pygame.time.Clock()
lista_geral = []
comprimento_inicial = 5
velocidade = 10
x_controle = velocidade
y_controle = 0
morreu = False
def aumenta_cobra(lista_geral):
    for XeY in lista_geral:
        pygame.draw.rect(tela, (0,255,0), (XeY[0],XeY[1], 20, 20))
def reiniciar_jogo():
    global aux, comprimento_inicial, x_cobra, x_maca,y_cobra, y_maca,lista, lista_geral, morreu
    aux = 0
    comprimento_inicial = 5
    x_cobra = largura/2
    y_cobra = altura/2
    x_maca= randint(40,600)
    y_maca = randint(50,450)
    lista = []
    lista_geral = []
    morreu = False


while True:
    mensagem = f'Pontos:{pontos}'
    texto = fonte.render(mensagem,True,(255,255,255))
    relogio.tick(20)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
        if event.type == KEYDOWN: 
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            elif event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            elif event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = -velocidade
            elif event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = velocidade
    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle
    ''' if pygame.key.get_pressed()[K_a]:
        x_cobra-=20
    elif pygame.key.get_pressed()[K_d]:
        x_cobra+=20
    elif pygame.key.get_pressed()[K_w]:
        y_cobra-=20
    elif pygame.key.get_pressed()[K_s]:
        y_cobra+=20'''

    cobra = pygame.draw.rect(tela,(0,255,0), (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.circle(tela,(255,0,0), (x_maca, y_maca), 10)
    if cobra.colliderect(maca):
        colisao.play()
        pontos+=1
        x_maca = randint(40,600)
        y_maca = randint(50,450)
        comprimento_inicial+=1
    lista = []
    lista.append(x_cobra)
    lista.append(y_cobra)
    lista_geral.append(lista)
    if lista_geral.count(lista) > 1:
        fonte2 = pygame.font.SysFont('arial', 20,True,True)
        mensagem2 = 'GAME OVER !! Precione a tecla R para jogar novamente'
        texto_formatado = fonte2.render(mensagem2, True, (0,0,0))
        ret_texto = texto_formatado.get_rect()
        morreu = True
        while morreu:
            tela.fill((200,200,200))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update() 
    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0
    if len(lista_geral)> comprimento_inicial:
        del lista_geral[0]
    aumenta_cobra(lista_geral)
    tela.blit(texto,(430,30))
    pygame.display.update()