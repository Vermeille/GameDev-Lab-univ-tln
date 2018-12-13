import pygame
import time
import vec
from types import SimpleNamespace

def ball(x, y, r):
    b = SimpleNamespace()
    b.forces = vec.vec(0, 0)
    b.speed = vec.vec(0, 0)
    b.pos = vec.vec(x, y)
    b.radius = r
    return b


def zero_forces(bs):
    for b in bs:
        b.forces = vec.vec(0, 0)


def integrate(bs):
    for b in bs:
        b.speed = vec.add(b.speed, b.forces)
        b.speed = vec.scale(b.speed, 0.99)
        b.pos = vec.add(b.pos, b.speed)


def wall_collisions(bs):
    collided = False
    for b in bs:
        if b.pos.y + b.radius > H:
            b.speed.y = -b.speed.y
            b.pos.y = H - b.radius - 1
            collided = True

        if b.pos.y - b.radius < 0:
            b.speed.y = -b.speed.y
            b.pos.y = b.radius + 1
            collided = True

        if b.pos.x + b.radius > W:
            b.speed.x = -b.speed.x
            b.pos.x = W - b.radius - 1
            collided = True

        if b.pos.x - b.radius < 0:
            b.speed.x = -b.speed.x
            b.pos.x = b.radius + 1
            collided = True
    return collided


def balls_collisions(balls):
    collided = False
    for b1 in balls:
        for b2 in balls:
            if b1 is b2:
                continue

            d = vec.sub(b1.pos, b2.pos)
            penetration = (b1.radius + b2.radius) - vec.len(d)
            if penetration < 0:
                continue

            collided = True
            n = vec.unit(d)
            b1.pos = vec.add(b1.pos, vec.scale(n, penetration / 2 + 1))
            b2.pos = vec.add(b2.pos, vec.scale(n, -penetration / 2 - 1))

            j = vec.dot(vec.sub(b2.speed, b1.speed), n) / 1
            b1.speed = vec.add(b1.speed, vec.scale(n, j))
            b2.speed = vec.add(b2.speed, vec.scale(n, -j))

    return collided


pygame.init()

W = 1600
H = 1200
screen = pygame.display.set_mode((W, H))

balls = [ball(400, 300, 30),
        ball(50, 50, 10),
        ball(150, 300, 15),
        ball(250, 300, 15),
        ball(300, 300, 35)]

while True:
    screen.fill((0, 0, 0))

    pygame.event.pump()
    if pygame.event.peek(pygame.QUIT):
        break

    keys = pygame.key.get_pressed()

    zero_forces(balls)

    if keys[pygame.K_LEFT]:
        balls[0].forces.x -= 1
    if keys[pygame.K_RIGHT]:
        balls[0].forces.x += 1
    if keys[pygame.K_UP]:
        balls[0].forces.y -= 1
    if keys[pygame.K_DOWN]:
        balls[0].forces.y += 1

    integrate(balls)

    collisions = True
    while collisions:
        collisions = wall_collisions(balls)
        collisions = balls_collisions(balls) or collisions

    for b in balls:
        pygame.draw.circle(
                screen,
                (255, 255, 255),
                (int(b.pos.x), int(b.pos.y)),
                b.radius)

    pygame.display.flip()
    time.sleep(1 / 60)
