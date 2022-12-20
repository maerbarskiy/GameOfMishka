import pygame
import COLORS
pygame.init()

sc = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game Of  Mishka")
pygame.display.set_icon(pygame.image.load("icon.bmp"))
clock = pygame.time.Clock()
FPS = 60

pygame.draw.rect(sc, COLORS.WHITE, (210, 150, 400, 300))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    clock.tick(FPS)