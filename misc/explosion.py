import pocketgl as gl
from types import SimpleNamespace
import time
import math
from random import uniform, gauss

gl.init_window('Win', 800, 600, 'sky blue')

def vec(x, y):
    v = SimpleNamespace()
    v.x = x
    v.y = y
    return v

def vec_add(u, v):
    return vec(u.x + v.x, u.y + v.y)

def particles_circle():
    particle = SimpleNamespace()
    particle.pos = vec(400, 300)
    particle.speed = vec(gauss(0, 5), gauss(0, 5))
    particle.duration = uniform(0, 1.5)
    particle.lifetime = 0
    return particle

def particle_update(p, wind_force):
    p.lifetime += 1/60
    p.pos = vec_add(p.pos, p.speed)
    p.speed.x *= 0.93
    p.speed.y *= 0.93

def alive_particles(ps):
    alive = []
    for p in ps:
        if p.duration > p.lifetime:
            alive += [p]
    return alive

nb_particles = 300
particles = []
for i in range(nb_particles//2):
    particles += [particles_circle()]

t = 0
timer = 0
while True:
    gl.clear_screen()

    for p in reversed(particles):
        gl.current_color(255, int(255 - p.lifetime * (255 // p.duration)), 0)
        gl.disc(p.pos.x, p.pos.y, 30 * (0.1 + (p.duration-p.lifetime)/p.duration))

    for p in particles:
        particle_update(p, math.sin(t)/2 + 0.5)

    particles = alive_particles(particles)
    timer += 1/60
    if timer > 2:
        for i in range(nb_particles - len(particles)):
            particles += [particles_circle()]
        timer = 0

    gl.refresh()
    time.sleep(1/60)
    t += 1/60
