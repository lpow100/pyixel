import pygame as pg
import math
from vector import *
from rgb import *
from errors import *

WHITE = Color(0,0,0,255)
RED = Color(255,0,0,255)
BLUE = Color(0,0,255,255)
GREEN = Color(0,255,0,255)
ORANGE = Color(255,165,0,255)
YELLOW = Color(255,255,0,255)
PURPLE = Color(255,0,255,255)
BLACK = Color(0,0,0,255)
BROWN = Color(160,82,45,255)
GRAY = Color(128,128,128,255)

"""a simple window for your game.
init with init_window for good init"""
class window:
    def __init__(self,screen:pg.Surface,pixelsize:vector2) -> None:
        self.__screen__ = screen
        self.pixels = [[]]
        for x in range(pixelsize.x-1):
            for y in range(pixelsize.y):
                self.pixels[-1].append(WHITE)
            self.pixels.append([])
        #pixels saved as [x][y]
        self.pixel_size = pixelsize
        self.events = []
    def draw_rect(self,color:Color,x:int,y:int,width:int,height:int):
        if x < 0 or x + width > self.pixel_size.x:
            raise outOfBoundsError(x,0,self.pixel_size.x)
        if y < 0 or y + height > self.pixel_size.y:
            raise outOfBoundsError(y,0,self.pixel_size.y)
        for xinc in range(x,x+width+1):
            for yinc in range(y,y+height+1):
                self.pixels[xinc][yinc] = color
    def draw_line(self,color:Color,x_start:int,y_start:int,x_end:int,y_end:int):
        if x_start < 0 or x_start > self.pixel_size.x:
            raise outOfBoundsError(x_start,0,self.pixel_size.x)
        if y_start < 0 or y_start > self.pixel_size.x:
            raise outOfBoundsError(y_start,0,self.pixel_size.y)
        if x_end < 0 or  x_end > self.pixel_size.x:
            raise outOfBoundsError(x_end,0,self.pixel_size.x)
        if y_end < 0 or y_end >  self.pixel_size.y:
            raise outOfBoundsError(y_end,0,self.pixel_size.y)
        line_len = ((x_end - x_start) ** 2 + (y_end - y_start) ** 2) ** 0.5
        for i in range(1,abs(int(line_len))):
                self.pixels[x_start + int((x_end - x_start) * (i / line_len))][y_start + int((y_end - y_start) * (i / line_len))] = color
    def draw_pixel(self,color:Color,x:int,y:int):
        if x < 0 or x > self.pixel_size.x:
            raise outOfBoundsError(x,0,self.pixel_size.x)
        if y < 0 or y > self.pixel_size.y:
            raise outOfBoundsError(y,0,self.pixel_size.y)
        self.pixels[x][y] = color
    def draw_circle(self,color:Color,x:int,y:int,radius:int):
        if x - radius < 0 or x + radius > self.pixel_size.x:
            raise outOfBoundsError(x,0,self.pixel_size.x)
        if y - radius < 0 or y + radius > self.pixel_size.y:
            raise outOfBoundsError(y,0,self.pixel_size.y)
        for r in range(radius + 1):
            for i in range(360):
                newx = int(math.cos(math.radians(i)) * r) + x
                newy = int(math.sin(math.radians(i)) * r) + y
                self.pixels[newx][newy] = color
    def draw_poly(self, color: Color, x: int, y: int, points: int, size: int, angle: int = 0):
        """Broken and I just cannot fix this RN :("""
        # Check if the polygon is within the bounds
        if x - size < 0 or x + size > self.pixel_size.x:
            raise outOfBoundsError(x, 0, self.pixel_size.x)
        if y - size < 0 or y + size > self.pixel_size.y:
            raise outOfBoundsError(y, 0, self.pixel_size.y)

        # Draw the polygon by connecting lines between calculated points
        for r in range(size):  # Draw concentric polygons based on size
            for i in range(points):
                # Calculate the current point (x1, y1)
                x1 = int(math.cos(math.radians(360 * (i / points) + angle)) * r) + x
                y1 = int(math.sin(math.radians(360 * (i / points) + angle)) * r) + y
                
                # Calculate the next point (x2, y2)
                x2 = int(math.cos(math.radians(360 * ((i + 1) / points) + angle)) * r) + x
                y2 = int(math.sin(math.radians(360 * ((i + 1) / points) + angle)) * r) + y
                
                # Draw the line between the two points
                self.draw_line(color, x1, y1, x2, y2)
        
    def clear_screen(self,bgcolor:Color):
        self.pixels = [[bgcolor for x in range(self.pixel_size.y)] for y in range(self.pixel_size.x)]
    def update(self):
        width,height = pg.display.get_surface().get_size()
        xscale,yscale = width/self.pixel_size.x, height/self.pixel_size.y
        for x in range(self.pixel_size.x-1):
            for y in range(self.pixel_size.y-1):
                pg.draw.rect(self.__screen__,self.pixels[x][y].tuple(),(x*xscale,y*yscale,xscale,yscale))
        pg.display.flip()
        self.events = pg.event.get()
    def running(self)->bool:
        for event in self.events:
            if event.type == pg.QUIT:
                return False
        return True

def init_window(width:int,height:int,xpixels:int,ypixels:int,name:str="")->window:
    pg.init()
    win = window(pg.display.set_mode((width,height)),vector2(xpixels,ypixels))
    if name != "":
        pg.display.set_caption(name)
    return win

def quit():
    pg.quit()
    