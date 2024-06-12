import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return Vector2D(self.x*other.x, self.y * other.y)
    
    def __truediv__(self, other):
        return Vector2D(self.x / other.x, self.y / other.y)
    
    def __neg__(self):
        return Vector2D(-self.x, -self.y)
    
    def __eq__(self, other):
        if isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
        return False
    
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        
    def __str__(self):
        return '({},{})'.format(self.x, self.y)
    

class Line2D:
    def __init__(self, start, end):
        self.__start = start
        self.__end = end

    def __len__(self):
        return int(math.sqrt((self.__start.x - self.__end.x)**2 + (self.__start.y -self.__end.y)**2))
    
    def __eq__(self, other):
        if isinstance(other, Line2D):
            return(self.__start == other.__start and self.__end == other.__end)
        else:
            return False
        
    def __lt__(self, other):
        return len(self) < len(other)
    
    def __le__(self, other):
        return len(self) <= len(other)
    
    def __gt__(self, other):
        return len(self) > len(other)
    
    def __ge__(self, other):
        return len(self) >= len(other)
    
    def __str__(self):
        return('{}, {}'.format(self.__start, self.__end))
        
v1 = Vector2D(10, 20)
v2 = Vector2D(2, 5) 

line1 = Line2D(v1, v2)

print(v1, '+', v2, '=', v1.__add__(v2))
print(v1, '-', v2, '=', v1.__sub__(v2))
print(v1, '*', v2, '=', v1.__mul__(v2))
print(v1, '/', v2, '=', v1.__truediv__(v2))
print('-',v1, '=', -v1)
print(v1, '==', v2, '=', v1.__eq__(v2))  
print(v1, '==', v1, '=', v1.__eq__(v1))  
print(v1, '==', 10, '=', v1.__eq__(10))  
print(v1,'과', v2,'의 거리', v1.distance(v2))

print('line1: {}'.format(line1))
print('line1의 길이: {}'.format(len(line1)))

v3_x = int(input('line1의 좌표1의 x값: '))
v3_y = int(input('line1의 좌표1의 y값: '))
v4_x = int(input('line2의 좌표2의 x값: '))
v4_y = int(input('line2의 좌표1의 y값: '))

v3 = Vector2D(v3_x, v3_y)
v4 = Vector2D(v4_x, v4_y)
line2 = Line2D(v3, v4)

print('line2: {}'.format(line2))
print('line2의 길이: {}'.format(len(line2)))

print('lin1 == line2 = {}'.format(line1 == line2))
print('lin1 < line2 = {}'.format(line1 < line2))
print('lin1 <= line2 = {}'.format(line1 <= line2))
print('lin1 > line2 = {}'.format(line1 > line2))
print('lin1 >= line2 = {}'.format(line1 >= line2))

print('20210591 조상원')
