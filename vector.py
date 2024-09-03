class vector2:
    def __init__(self,x:float,y:float) -> None:
        self.x = x
        self.y = y
    def __add__(self, other):
        self.x += other.x
        self.y += other.y
    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y
    def __mul__(self, other):
        self.x *= other.x
        self.y *= other.y
    def __truediv__(self, other):
        self.x /= other.x
        self.y /= other.y
    def __floordiv__(self, other):
        self.x //= other.x
        self.y //= other.y
    def __mod__(self, other):
        self.x %= other.x
        self.y %= other.y
    def __pow__(self, other):
        self.x **= other.x
        self.y **= other.y
    def normalize(self):
        self.x = self.x/abs(self.x)
        self.y = self.y/abs(self.y)
    def length(self) -> float:
        return (self.x**2+self.y**2)**(1/2)
   
#ima save this code but it's a 2d farmework so we don't need it :( 
"""class vector3:
    def __init__(self,x:float,y:float) -> None:
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
    def __mul__(self, other):
        self.x *= other.x
        self.y *= other.y
        self.z *= other.z
    def __truediv__(self, other):
        self.x /= other.x
        self.y /= other.y
        self.z /= other.z
    def __floordiv__(self, other):
        self.x //= other.x
        self.y //= other.y
        self.z //= other.z
    def __mod__(self, other):
        self.x %= other.x
        self.y %= other.y
        self.z %= other.z
    def __pow__(self, other):
        self.x **= other.x
        self.y **= other.y
        self.z **= other.z
    def normalize(self):
        self.x = self.x/abs(self.x)
        self.y = self.y/abs(self.y)
        self.z = self.z/abs(self.z)
    def length(self) -> float:
        return (self.x**2+self.y**2+self.z**2)**(1/2)"""