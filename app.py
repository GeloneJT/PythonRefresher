'''Python Classes: Magic Methods'''


class Point:
    '''create custom class Point'''

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        '''Adds the points'''
        return Point(self.x + other.x, self.y + other.y)


point = Point(10, 20)
another = Point(1, 2)
combined = point + another
print(combined.x)
