import pygame

pygame.init()
width, height = 514, 800
backgroundColor = 255, 0, 0

screen = pygame.display.set_mode((width, height))

mcduframe = pygame.image.load("TEMOMCDU.png")
framerect = mcduframe.get_rect()

while True:
  screen.fill(backgroundColor)
  screen.blit(mcduframe, framerect)
  pygame.display.flip()


