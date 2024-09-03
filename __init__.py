import pygame as pg
from vector import *
from rgb import *

WHITE = Color(0,0,0,255)
RED =
BLUE =
GREEN =
ORANGE =


"""a simple window for your game.
init with init_window for good init"""
class window:
    def __init__(self,screen,pixelsize:vector2) -> None:
        self.__screen__ = screen
        self.pixels = [[]]
    def draw_rect(self,color:Color,x:int,y:int,width:int,height:int):
    

def init_window(width:int,height:int,xpixels:int,ypixels:int,name:str="")->window:
    pg.init()
    window(pg.display.set_mode((width,height)))
    if name != "":
        pg.display.set_caption(name)
    return window

    