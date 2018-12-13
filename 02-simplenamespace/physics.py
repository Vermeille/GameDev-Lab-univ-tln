import pygame
import time
from vec import *

pygame.init()

W = 800
H = 600
screen = pygame.display.set_mode((W, H))

pos = vec(400, 300)
speed = vec(0, 0)
while True:
    screen.fill((0, 0, 0))

    pygame.event.pump()
    if pygame.event.peek(pygame.QUIT):
        break

    keys = pygame.key.get_pressed()

    forces = vec(0, 0)
    if keys[pygame.K_LEFT]:
        forces.x -= 1
    if keys[pygame.K_RIGHT]:
        forces.x += 1
    if keys[pygame.K_UP]:
        forces.y -= 1
    if keys[pygame.K_DOWN]:
        forces.y += 1

    speed = vec_add(speed, forces)
    speed = vec_scale(speed, 0.95)
    pos = vec_add(pos, speed)

    pygame.draw.circle(
            screen,
            (255, 255, 255),
            (int(pos.x), int(pos.y)),
            50)

    pygame.display.flip()
    time.sleep(1 / 60)
