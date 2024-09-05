class vector2:
    def __init__(self,x:float,y:float) -> None:
        self.x = x
        self.y = y
    def __add__(self, other):
        new = vector2(0,0)
        new.x += other.x
        new.y += other.y
        return new
    def __sub__(self, other):
        new = vector2(0,0)
        new.x -= other.x
        new.y -= other.y
        return new
    def __mul__(self, other):
        new = vector2(0,0)
        new.x *= other.x
        new.y *= other.y
        return new
    def __truediv__(self, other):
        new = vector2(0,0)
        new.x /= other.x
        new.y /= other.y
        return new
    def __floordiv__(self, other):
        new = vector2(0,0)
        new.x //= other.x
        new.y //= other.y
        return new
    def __mod__(self, other):
        new = vector2(0,0)
        new.x %= other.x
        new.y %= other.y
        return new
    def __pow__(self, other):
        new = vector2(0,0)
        new.x **= other.x
        new.y **= other.y
        return new
    def normalized(self):
        new = vector2(0,0)
        new.x = self.x/abs(self.x)
        new.y = self.y/abs(self.y)
        return new
    def scaled(self,a:float):
        return vector2(self.x*a,self.y*a)
    def length(self) -> float:
        return (self.x**2+self.y**2)**(1/2)
   
#ima save this code but it's a 2d farmework so we don't need it :( 
"""class vector3:
    def __init__(self,x:float,y:float) -> None:
        new.x = x
        new.y = y
        new.z = z
    def __add__(self, other):
        new.x += other.x
        new.y += other.y
        new.z += other.z
    def __sub__(self, other):
        new.x -= other.x
        new.y -= other.y
        new.z -= other.z
    def __mul__(self, other):
        new.x *= other.x
        new.y *= other.y
        new.z *= other.z
    def __truediv__(self, other):
        new.x /= other.x
        new.y /= other.y
        new.z /= other.z
    def __floordiv__(self, other):
        new.x //= other.x
        new.y //= other.y
        new.z //= other.z
    def __mod__(self, other):
        new.x %= other.x
        new.y %= other.y
        new.z %= other.z
    def __pow__(self, other):
        new.x **= other.x
        new.y **= other.y
        new.z **= other.z
    def normalize(self):
        new.x = new.x/abs(new.x)
        new.y = new.y/abs(new.y)
        new.z = new.z/abs(new.z)
    def length(self) -> float:
        return (new.x**2+new.y**2+new.z**2)**(1/2)"""