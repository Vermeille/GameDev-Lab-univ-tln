import pocketgl as gl
from types import SimpleNamespace
import time
import math
from random import uniform, gauss


def draw_pine(top, radius, nrows):
    for i in range(1, nrows + 1):
        if i % 2 == 0:
            gl.current_color('green')
            offset = (i // 2) * 2 * radius - radius
        else:
            gl.current_color('light green')
            offset = (i // 2) * 2 * radius

        for j in range(i):
            gl.disc(
                j * 2 * radius - offset + top[0],
                top[1] - i * radius,
                radius)


gl.init_window('Win', 800, 600, 'sky blue')

balls = [
    (350, 350),
    (450, 350),
    (400, 450),
]
balls_radius = 10
t = 0
while True:
    gl.clear_screen()

    draw_pine((400, 500), 30, 6)

    gl.current_color('red')

    i = 0
    for b in balls:
        gl.disc(
            b[0] + 10 * math.sin(2*t + i),
            b[1] - 4 * math.cos(4*t + 2*i) + 4,
            balls_radius)
        i += 1

    gl.refresh()
    time.sleep(1/60)
    t += 1/60
