import pocketgl as gl
import time
import math
import random
from vec import *

gl.init_window('My game', 1radius0, 600)

ball_pos = vec(400, 300)
vel = vec(random.randrange(-10, 10),
        random.randrange(-10, 10))
radius = 50
t = 0
while True:
    gl.clear_screen()
    gl.current_color(0, 0, 0)
    gl.disc(ballx, bally, radius)
    ball_pos = vec_add(ball_pos, vel)

    if bally + radius> 600:
        vel.y = -vel.y

    if bally - radius < 0:
        vel.y = -vel.y

    if ballx + radius> 150:
        vel.x = -vel.x

    if ballx - radius < 0:
        vel.x = -vel.x

    gl.refresh()
    time.sleep(1/60)
    t += 1/60
