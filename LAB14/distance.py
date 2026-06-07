import math
def distance(p1,p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    return math.sqrt(dx**2 + dy**2)
def point(object):
    pass
p1 = point()
p1.x = 0
p1.y = 0

p2 = point()
p2.x = 4
p2.y = 3

print(distance(p1,p2))