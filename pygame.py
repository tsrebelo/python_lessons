import pygame
import sys

pygame.init()

largura, altura = 400, 300
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Exemplo simples com pygame")

cor_fundo = (100, 150, 200)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.exit()
            sys.exit()
    
    janela.fill(cor_fundo)
    pygame.display.flip()