import pygame
import time
import math

pygame.init()

W = 800
H = 600
screen = pygame.display.set_mode((W, H))

x = 400
t = 0
while True:
    screen.fill((0, 0, 0))

    pygame.event.pump()
    if pygame.event.peek(pygame.QUIT):
        break

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        x += 3

    pygame.draw.circle(
            screen,
            (255, 255, 255),
            (x + 50 * math.sin(t), 300),
            50)

    pygame.display.flip()
    time.sleep(1 / 60)
    t += 1 / 60
