import functools

test_tuple = (1, 4, 5) 
res = functools.reduce(lambda sub, ele: sub * 10 + ele, test_tuple)
res2 = [int(_) for _ in test_tuple] 
print(res2)

class Grid:
    def __init__(self,columns, rows, emptyValue):
        self.rows = rows
        self.columns = columns
        self.xy = list([[Cell([i,j], self, emptyValue) for j,_ in enumerate(range(columns))] for i,_ in enumerate(range(rows))])
        self.cells = []

    def cellSwap(self, a, b):
        
        xyA= functools.reduce(lambda sub, ele: sub * 10 + ele, a)
        xyB= functools.reduce(lambda sub, ele: sub * 10 + ele, b)
        del self.xy[xyA[:1]][xyA[1:]]
        """
        self.xy[xyA[:1]][xyA[1:]].xy, self.xy[xyB[:1]][xyB[1:]].xy = self.xy[xyB[:1]][xyB[1:]].xy, self.xy[xyA[:1]][xyA[1:]].xy
        self.xy[xyA[:1]][xyA[1:]].value, self.xy[xyB[:1]][xyB[1:]].value = self.xy[xyB[:1]][xyB[1:]].value, self.xy[xyA[:1]][xyA[1:]].value
        """

    def __str__(self):
        return str("\n".join(map(str, [[y.value for y in x] for x in self.xy])))

    def len(self):
        return self.height * self.width
        

#Parent
class Cell():
    def __init__(self, xy, grid, value):
        #xy->idx = y value    *    rows   + x value
        self.idx = xy[-1:][0] * grid.rows + xy[:1][0]
        #idx->xy      = [x = idx  /    rows  , y = idx  %   rows    ]
        self.location = [self.idx / grid.rows, self.idx % grid.rows,]
        self.grid = grid
        self.value = value
    
    @classmethod
    def __str__(cls):
        return str(cls.value)

    def setValue(self, val):
        self.value = val

    def setXy(self, xy):
        self.xy = xy
    
    def getXy(self, xy):
        return self.xy

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


test = Grid(20,10,' ')
f1 = Cell([0,2], test, 'F')
test.xy[0][0].setValue('F')
test.xy[1][0].setValue('X')
#test.insert(f1)



##test.xy[0][0], test.xy[1][0] = test.xy[1][0], test.xy[0][0]

#test.cellSwap([0,0],[1,0])
print(test)
print(test.xy[2][1].idx)

#print(test.cells)