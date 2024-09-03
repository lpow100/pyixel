class Color:
    def __init__(self,red:int,green:int,blue:int,alpha:int=255) -> None:
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha
    def tuple(self,include_alpha=False)->tuple:
        return (self.red,self.green,self.blue) if not include_alpha else (self.red,self.green,self.blue,self.alpha)
    def hex(self,include_alpha=False)->str:
        r = hex(self.red)[2:]
        r = r if len(r) == 2 else '0' + r
        g = hex(self.green)[2:]
        g = g if len(g) == 2 else '0' + g
        b = hex(self.blue)[2:]
        b = b if len(b) == 2 else '0' + b
        if not include_alpha:
            return '#'+r+g+b
        else:
            a = hex(self.alpha)[2:]
            a = a if len(a) == 2 else '0' + a
            return '#'+r+g+b+a
            