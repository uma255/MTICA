class vector2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,ob):
        return vector2D(self.x+ob.x,self.y+ob.y)
    def __sub__(self,other):
        return vector2D(self.x-other.x,self.y-other.y)
first=vector2D(5,7)
second=vector2D(3,8)
result=first+second
print(result.x)
print(result.y)
result=first-second
print(result.x)
print(result.y)
