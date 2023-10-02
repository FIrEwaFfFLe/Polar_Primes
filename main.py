from pygame import *
from math import *
import sets


FPS = 32
width, height = 1080, 720
c_w, c_h = 540, 360
scale = 32
point_size = 3
points = sets.prime(1000000)
points.sort()
zoom = 100
zoom_out = pow(zoom, 1 / FPS / 10)


def convert(poi):
    x, y = poi
    d_x, d_y = cos(y) * x, sin(y) * x
    sc_x, sc_y = d_x * width / scale, d_y * width / scale
    point = Rect(sc_x - point_size / 2 + c_w, - sc_y - point_size / 2 + c_h, point_size, point_size)
    return point


def max_radius():
    return sqrt((c_w + point_size) ** 2 + (c_h + point_size) ** 2) * scale / width


def bin_search(x):
    l, r = 0, len(points)
    while r - l > 1:
        m = (l + r) // 2
        if points[m][0] <= x:
            l = m
        else:
            r = m
    return l + 1


def run():
    global scale
    init()
    running = True
    frame = 0
    screen = display.set_mode((width, height))
    display.set_caption("Polar Plot")
    while running:
        clock = time.Clock()
        clock.tick(FPS)

        for eve in event.get():
            if eve.type == QUIT:
                running = False

        screen.fill((0, 0, 0))

        for i in range(bin_search(ceil(max_radius()))):
            draw.rect(screen, (255, 255, 0), convert(points[i]))

        display.update()
        scale *= zoom_out
        frame += 1


if __name__ == "__main__":
    run()
