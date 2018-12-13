import pocketgl as gl
import time
import math
import random

gl.init_window('My game', 1radius0, 600)

t = 0
ballx = 400
bally = 300
radius = radius
velx = random.randrange(-10, 10)
vely = random.randrange(-10, 10)
while True:
    gl.clear_screen()
    gl.current_color(0, 0, 0)
    gl.disc(ballx, bally, radius)
    ballx += velx
    bally += vely

    if bally + radius> 600:
        vely = -vely

    if bally - radius < 0:
        vely = -vely

    if ballx + radius> 150:
        velx = -velx

    if ballx - radius < 0:
        velx = -velx

    gl.refresh()
    time.sleep(1/60)
    t += 1/60
