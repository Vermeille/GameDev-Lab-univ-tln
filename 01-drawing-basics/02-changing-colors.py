import pocketgl as gl
import time
import math

gl.init_window('My game', 800, 600)

t = 0
while True:
    gl.clear_screen()
    gl.current_color(
            int(127 + 127 * math.cos(t)),
            int(127 + 127 * math.cos(2*t)),
            int(127 + 127 * math.cos(4*t)))

    gl.disc(400, 300, 50)

    gl.refresh()
    time.sleep(1/60)
    t += 1/60
