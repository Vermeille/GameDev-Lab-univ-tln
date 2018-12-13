from types import SimpleNamespace


def vec(x, y):
    u = SimpleNamespace()
    u.x = x
    u.y = y
    return u


def vec_add(u, v):
    return vec(u.x + v.x, u.y + v.y)


def vec_sub(u, v):
    return vec(u.x - v.x, u.y - v.y)


def vec_scale(u, s):
    return vec(s * u.x, s * u.y)


def vec_dot(u, v):
    return u.x * v.x + u.y * v.y


def vec_sqlen(u):
    return u.x * u.x + u.y * u.y


def vec_len(u):
    return vec_sqlen(u) ** 0.5

