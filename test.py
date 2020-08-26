import functools

test_tuple = (1, 4, 5) 
res = functools.reduce(lambda sub, ele: sub * 10 + ele, test_tuple)
res2 = [int(_) for _ in test_tuple] 
print(res2)

class Grid:
    def __init__(self, rows, columns, emptyValue):
        self.body = list([[Cell([-1,-1], self, '.') for _ in range(rows)] for _ in range(columns)])
        self.rows = rows
        self.columns = columns
        self.cells = []

    def insert(self, cell):
        self.body[cell.getX()][cell.getY()] = cell.value

    def __str__(self):
        return '\n'.join(map(str, self.body))

    def len(self):
        return self.height * self.width
        

#Parent
class Cell():
    def __init__(self, xy, grid, value):
        self.xy = xy
        self.grid = grid
        self.value = value
    
    @classmethod
    def __str__(cls):
        return str(cls.value)

    def getX(self):
        return [int(self.xy[:1])]

    def getY(self):
        return [int(self.xy[1:])]

    def getLocation(self):
        return [int(_) for _ in self.location] 

    @classmethod
    def setLocation(cls, arr):
        cls.location = tuple(arr) 

    @classmethod
    def insert(cls):
        cls.matrix[cls.x][cls.y] = cls.value

"""
class Faller(Cell):
    def __init__(self, location, grid, value = 'F'):
        super(Faller, self).__init__(location, grid, value).getLocation()

    def fall(self):
        if self.grid[self.x][self.y + 1] == ".":
            self.grid[self.x][self.y] = "."
            self.y = self.y + 1
            self.insert()

"""

    


matrix = []
rows = 20


for i in range(rows):
    matrix.append(["."] * 20)
matrix[8][2] = "X"






test = Grid(20,10,'.')
f1 = Cell([0,2], test, 'F')
#test.insert(f1)
print(test)
print(test.cells)