import pocketgl as gl
import time
import math
import random

gl.init_window('My game', 1500, 600)

t = 0
ballx = 400
bally = 300
velx = random.randrange(-10, 10)
vely = random.randrange(-10, 10)
while True:
    gl.clear_screen()
    gl.current_color(0, 0, 0)
    gl.disc(ballx, bally, 50)
    ballx += velx
    bally += vely

    if bally + 50> 600:
        vely = -vely

    if bally - 50 < 0:
        vely = -vely

    if ballx + 50> 1500:
        velx = -velx

    if ballx - 50 < 0:
        velx = -velx

    gl.refresh()
    time.sleep(1/60)
    t += 1/60
