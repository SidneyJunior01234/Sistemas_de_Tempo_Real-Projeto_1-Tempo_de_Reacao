import pygame
import sys
import time
import random
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Trabalho 01 - Reação de Movimento')

centro_tela = pygame.Vector2(DISPLAYSURF.get_width() / 2, DISPLAYSURF.get_height() / 2)
bordas_finais = pygame.Vector2(DISPLAYSURF.get_width(), DISPLAYSURF.get_height())

comandos_cores = {
  0: [pygame.K_UP, 'blue', pygame.Rect(0, 0, centro_tela.x, centro_tela.y)],
  1: [pygame.K_RIGHT, 'green', pygame.Rect(centro_tela.x, 0, bordas_finais.x, centro_tela.y)],
  2: [pygame.K_LEFT, 'red', pygame.Rect(0, centro_tela.y, centro_tela.x, bordas_finais.y)],
  3: [pygame.K_DOWN, 'yellow',pygame.Rect(centro_tela.x, centro_tela.y, bordas_finais.x, bordas_finais.y)]
}

font = pygame.font.Font('freesansbold.ttf', 12)

tempo_reacao = 0.0
cor_aleatoria = 0
ultima_cor = cor_aleatoria
tempo_inicial = 0
tempo_final = 0
tempo_total = 0
acertos = 0
erros = 0

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      entrada = pygame.key.get_pressed()
      if entrada[comandos_cores[cor_aleatoria][0]]:
        if tempo_inicial == 0:
          tempo_inicial = time.time()
        else:
          tempo_final = time.time()
          tempo_reacao = tempo_final - tempo_inicial
          tempo_inicial = tempo_final
          tempo_total += tempo_reacao
          acertos += 1
      else:
        erros += 1

      cor_aleatoria = random.randint(0, 3)
      while cor_aleatoria == ultima_cor:
        cor_aleatoria = random.randint(0, 3)
      ultima_cor = cor_aleatoria

  DISPLAYSURF.fill('gray')
  pygame.draw.rect(DISPLAYSURF, comandos_cores[cor_aleatoria][1], comandos_cores[cor_aleatoria][2])

  text = font.render(f'Tempo Médio de Reação: {tempo_total / max(1, acertos):.2f} segundos', True, 'black', 'gray')
  text2 = font.render(f'Acertos: {acertos} Erros: {erros}', True, 'black', 'gray')

  textRect = text.get_rect()
  textRect.center = (centro_tela.x, centro_tela.y - 15)
  text2Rect = text2.get_rect()
  text2Rect.center = (centro_tela.x, centro_tela.y + 15)

  DISPLAYSURF.blit(text, textRect)
  DISPLAYSURF.blit(text2, text2Rect)

  pygame.display.flip()
  pygame.display.update()
