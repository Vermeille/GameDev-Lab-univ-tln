from types import SimpleNamespace


def vec(x, y):
    u = SimpleNamespace()
    u.x = x
    u.y = y
    return u


def add(u, v):
    return vec(u.x + v.x, u.y + v.y)


def sub(u, v):
    return vec(u.x - v.x, u.y - v.y)


def scale(u, s):
    return vec(s * u.x, s * u.y)


def dot(u, v):
    return u.x * v.x + u.y * v.y


def sqlen(u):
    return u.x * u.x + u.y * u.y


def unit(u):
    l = len(u)
    return vec(u.x / l, u.y / l)


def len(u):
    return sqlen(u) ** 0.5

