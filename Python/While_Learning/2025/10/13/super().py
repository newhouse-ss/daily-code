class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        #用super调用父类中的函数
        super().__init__(color, is_filled)
        self.radius = radius

circle = Circle("Blue", True, 9)
print(circle.color)
print(circle.is_filled)