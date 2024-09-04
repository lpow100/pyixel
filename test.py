import __init__ as pyixel
from random import randint

win = pyixel.init_window(800,400,200,100,"Test")


win.clear_screen(pyixel.WHITE)
win.draw_rect(pyixel.BLUE,randint(0,150),randint(0,50),20,20)
win.draw_line(pyixel.GREEN,randint(0,199),randint(0,99),randint(0,199),randint(0,99))
win.draw_pixel(pyixel.RED,randint(0,199),randint(0,99))
win.update()
while win.running():
    win.update()
pyixel.quit()