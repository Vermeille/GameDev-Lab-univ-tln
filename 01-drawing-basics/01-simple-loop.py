import pocketgl as gl
import time
import math

gl.init_window('My game', 800, 600)

t = 0
while True:
    gl.clear_screen()
    gl.current_color(0, 0, 0)

    gl.disc(400 + 200*math.cos(5*t), 300, 50)

    gl.refresh()
    time.sleep(1/60)
    t += 1/60
