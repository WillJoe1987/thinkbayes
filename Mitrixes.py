import random
class point():
    left = 0
    right = 0
    top = 0
    buttom  = 0
    x = 0
    y = 0
    Matrix = None

    def __init__(self, x, y, mitrix):
        self.left = random.random()
        self.right = random.random()
        self.top = random.random()
        self.buttom = random.random()
        self.x = x
        self.y = y
        self.Matrix = mitrix

    def get_right(self):
        return self.left + self.right + self.buttom + self.top

    def update(self):
        up = self.Matrix.get_up(self)
        down = self.Matrix.get_down(self)
        left = self.Matrix.get_left(self)
        right = self.Matrix.get_right(self)
        self.left = self.function(left, right,up, down) * self.left
        self.right = self.function(right, up, down, left ) * self.right
        self.top = self.function(up, down, left, right) * self.top
        self.buttom = self.function(down, left, right,up ) * self.buttom

    def function(self, up, down, left, right):
        return up.get_right()/(up.get_right()+ down.get_right() + left.get_right() + right.get_right())

    def print(self):
        print('x:'+str(self.x) + ';y:'+str(self.y) + ';right:'+str(self.get_right()))

class Mitrix():

    def __init__(self, x, y):
        self.points = [[0 for i in range(x)] for i in range(y)]
        for i in range(x):
            for j in range(y):
                self.points[i][j] = point(i,j, self)

    def get_left(self, point):
        x = 0
        if point.x == 0 :
            x = len(self.points[0]) -1
        else :
            x = point.x - 1
        y = 0
        return self.get_point(x, point.y)

    def get_right(self, point):
        x = 0
        if point.x == len(self.points[0])-1:
            x = 0
        else :
            x = point.x + 1
        return self.get_point(x, point.y)

    def get_up(self, point):
        y = 0
        if point.y == 0:
            y = len(self.points) - 1
        else :
            y = point.y - 1
        return self.get_point(point.x, y)

    def get_down(self, point):
        y = 0
        if point.y == len(self.points) - 1:
            y = 0
        else:
            y = point.y + 1
        return self.get_point(point.x, y)

    def get_point(self, x, y):
        return self.points[x][y]

    def print_points(self):
        for r in self.points :
            for point in r :
                point.print()

    def update_all(self):
        for r in self.points :
            for point in r :
                point.update()


m = Mitrix(3,3)
print(m)
m.print_points()
m.update_all()
print(m)
m.print_points()


for x in range(100):
    print("====="+str(x)+"=========")
    m.print_points()