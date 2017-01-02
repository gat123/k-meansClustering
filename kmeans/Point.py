import math

class Point:
    def __init__(self, coords):
        self.coords = coords
        self.n = len(coords)

    def __getitem__(self, i):
        return self.coords[i]

    def equals(self, point):
        for dim_1, dim_2 in zip(self.coords, point):
            if dim_1 != dim_2:
                return False
        return True

    def getDistance(self, coords):

        if coords.n != self.n:
            raise Exception("ILLEGAL: wrong dimensions")

        points = [(self.coords[i], coords[i]) for i in xrange(self.n)]
        dist = [(a - b)**2 for a, b in points]
        dist = math.sqrt(sum(dist))

        return dist

    def __repr__(self):
        return str(self.coords)

