from types import SimpleNamespace

def vec(x, y):
    u = SimpleNamespace()
    u.x = x
    u.y = y
    return u


u = vec(3, 4)
print(u)
