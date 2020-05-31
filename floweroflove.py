

import tkinter
import time


CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
PETAL = 100
PETAL_SPACE = PETAL / 2
DIA = PETAL / 2
CENTER_X = CANVAS_WIDTH / 2 - PETAL / 2
CENTER_Y = CANVAS_HEIGHT / 2 - PETAL / 2

def main():
    # makes a canvas
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Flower Of Love')

    # this marks the center of the canvas
    x = CENTER_X
    y = CENTER_Y
    petal = PETAL
    quarter = DIA / 2
    fraction = quarter/3.5

    ##### CREATES FLOWER OF LIFE GRAPHIC #####

    # Creates petals in the center row
    petal_center1 = canvas.create_oval(x, y, x + petal, y + petal, fill='', outline='#ffc0cb', width= 5)
    petal_center2 = canvas.create_oval(x, y+DIA, x + petal, y + petal+DIA, fill='', outline='#ffc0cb', width= 5)
    petal_center3 = canvas.create_oval(x, y + petal, x + petal, y + petal * 2, fill='', outline='#ffc0cb', width=5)
    petal_center4 = canvas.create_oval(x, y + petal + DIA, x + petal, y + petal * 2 + DIA, fill='', outline='#ffc0cb', width=5)
    petal_center5 = canvas.create_oval(x, y + petal * 2, x + petal, y + petal * 3, fill='', outline='#ffc0cb',
                                       width=5)

    # Creates petals in the row to left, closest to center
    petal_L1 = canvas.create_oval(x - DIA + fraction, y + quarter * 1, (x - DIA) + petal + fraction,
                                 y + quarter * 1 + petal, fill='', outline='#ffc0cb', width=5)
    petal_L2 = canvas.create_oval(x - DIA + fraction, y + quarter * 3, (x - DIA) + petal + fraction,
                                  y + quarter * 3 + petal, fill='', outline='#ffc0cb', width=5)
    petal_L3 = canvas.create_oval(x - DIA + fraction, y + quarter * 5, (x - DIA) + petal + fraction,
                                  y + quarter * 5 + petal,
                                  fill='', outline='#ffc0cb', width=5)
    petal_L4 = canvas.create_oval(x - DIA + fraction, y + quarter * 7, (x - DIA) + petal + fraction,
                                  y + quarter * 7 + petal,
                                  fill='', outline='#ffc0cb', width=5)


    # Creates petals in the row to far right, farthest from center
    petal_R1 = canvas.create_oval(x + DIA - fraction, y + quarter * 1, (x + DIA) + petal - fraction,
                                  y + quarter * 1 + petal, fill='', outline='#ffc0cb', width=5)
    petal_R2 = canvas.create_oval(x + DIA - fraction, y + quarter * 3, x + DIA + petal - fraction,
                                  y + quarter * 3 + petal, fill='', outline='#ffc0cb', width=5)
    petal_R3 = canvas.create_oval(x + DIA - fraction, y + quarter * 5, x + DIA + petal - fraction,
                                  y + quarter * 5 + petal, fill='', outline='#ffc0cb', width=5)
    petal_R4 = canvas.create_oval(x + DIA - fraction, y + quarter * 7, x + DIA + petal - fraction,
                                  y + quarter * 7 + petal, fill='', outline='#ffc0cb', width=5)

    # Creates petals in the row to far right, closest to center
    petal_LL1 = canvas.create_oval(x - petal + fraction*2, y + quarter * 2, (x - petal + fraction * 2) + petal,
                                  y + quarter * 2 + petal, fill='', outline='#ffc0cb', width=5)
    petal_LL2 = canvas.create_oval(x - petal + fraction*2, y + quarter * 4, (x - petal + fraction * 2) + petal,
                                  y + quarter * 4 + petal, fill='', outline='#ffc0cb', width=5)
    petal_LL3 = canvas.create_oval(x - petal + fraction*2, y + quarter * 6, (x - petal + fraction * 2) + petal,
                                  y + quarter * 6 + petal,
                                  fill='', outline='#ffc0cb', width=5)

    # Creates petals in the row to right, farthest from center
    petal_RR1 = canvas.create_oval(x + petal - fraction * 2, y + quarter * 2, (x + petal - fraction * 2) + petal,
                                   y + quarter * 2 + petal, fill='', outline='#ffc0cb', width=5)
    petal_RR2 = canvas.create_oval(x + petal - fraction * 2, y + quarter * 4, (x + petal - fraction * 2) + petal,
                                   y + quarter * 4 + petal, fill='', outline='#ffc0cb', width=5)
    petal_RR3 = canvas.create_oval(x + petal - fraction * 2, y + quarter * 6, (x + petal - fraction * 2) + petal,
                                   y + quarter * 6 + petal,
                                   fill='', outline='#ffc0cb', width=5)


    dx = 3
    dy = 5

    while True:
        canvas.move(petal_center1, dx, dy)
        canvas.move(petal_center2, dx, dy)
        canvas.move(petal_center3, dx, dy)
        canvas.move(petal_center4, dx, dy)
        canvas.move(petal_center5, dx, dy)

        canvas.move(petal_R1, dx, dy)
        canvas.move(petal_R2, dx, dy)
        canvas.move(petal_R3, dx, dy)
        canvas.move(petal_R4, dx, dy)

        canvas.move(petal_L1, dx, dy)
        canvas.move(petal_L2, dx, dy)
        canvas.move(petal_L3, dx, dy)
        canvas.move(petal_L4, dx, dy)

        canvas.move(petal_LL1, dx, dy)
        canvas.move(petal_LL2, dx, dy)
        canvas.move(petal_LL3, dx, dy)

        canvas.move(petal_RR1, dx, dy)
        canvas.move(petal_RR2, dx, dy)
        canvas.move(petal_RR3, dx, dy)

        if hit_left_wall(canvas, petal_LL1) or hit_right_wall(canvas, petal_RR1):
            dx *= -1

        if hit_top_wall(canvas, petal_center1) or hit_bottom_wall(canvas, petal_center5):
            dy *= -1

        canvas.update()
        # pause
        time.sleep(1 / 50.)  # parameter is seconds to pause.
    canvas.mainloop()

def hit_left_wall(canvas, object):
    return get_left_x(canvas, object) <= 0

def hit_top_wall(canvas, object):
    return get_top_y(canvas, object) <= 0

def hit_right_wall(canvas, object):
    return get_right_x(canvas, object) >= CANVAS_WIDTH

def hit_bottom_wall(canvas, object):
    return get_bottom_y(canvas, object) >= CANVAS_HEIGHT


def get_left_x(canvas, object):
    return canvas.coords(object)[0]

def get_top_y(canvas, object):
    return canvas.coords(object)[1]

def get_right_x(canvas, object):
    return canvas.coords(object)[2]

def get_bottom_y(canvas, object):
    return canvas.coords(object)[3]


def make_canvas(width, height, title):
    """
    Creates and returns a drawing canvas
    of the given int size
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas


if __name__ == '__main__':
    main()
