import heapq
import math

class Djisktra:

    def __init__(self, gStart, gEnd, neighbours, obs):

        self.gStart = gStart
        self.gEnd = gEnd
        self.neighbours = neighbours
        self.gMap = {}
        self.obs = obs
        self.heap = []
        self.parent = {}
        self.visited = []

    def search(self):

        self.gMap[gStart] = 0
        self.parent[self.gStart] = self.gStart

        heapq.heappush(self.heap, (self.fFunc(self.gStart), self.gStart))

        self.visited.append(self.gStart)

        while len(self.heap) is not 0:

            currEle = heapq.heappop(self.heap)
            currPos = currEle[1]

            if currPos == self.gEnd:
                break

            for neighbour in self.neighbours[currPos]:

                if neighbour in self.visited:
                    continue

                if neighbour not in self.gMap:
                    self.gMap[neighbour] = math.inf

                gCost = self.gMap[currPos] + self.cost(currPos, neighbour)

                if gCost < self.gMap[neighbour]:

                    self.gMap[neighbour] = gCost
                    self.parent[neighbour] = currPos
                    heapq.heappush(self.heap, (self.gMap[neighbour], neighbour))

        return self.printPath()

    def fFunc(self, currPos):

        return self.gMap[currPos]

    def cost(self, currPos, neighbour):

        if neighbour in self.obs:
            return math.inf

        return 10

    def printPath(self):

        path = []
        currPos = self.gEnd
        path.append(currPos)

        while True:
            currPos = self.parent[currPos]

            if currPos == self.gStart:
                path.append(currPos)
                break
            path.append(currPos)

        return path, self.visited

class Space:

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.neighbours = {}
        self.obs = []

    def sweepSpace(self):

        for i in range(self.x):
            for j in range(self.y):

                self.neighboursFunc(i, j)

    def neighboursFunc(self, i, j):

        res = []

        if i - 1 >= 0 and j - 1 >= 0:
            res.append((i-1,j-1))

        if i + 1 <= self.x - 1 and j + 1 <= self.y - 1:
            res.append((i+1,j+1))

        if i - 1 >= 0:
            res.append((i-1,j))

        if j - 1 >= 0:
            res.append((i,j-1))

        if i + 1 <= self.x - 1:
            res.append((i+1,j))

        if j + 1 <= self.y - 1:
            res.append((i,j+1))

        if i + 1 <= self.x - 1 and j - 1 >= 0:
            res.append((i+1,j-1))

        if i - 1 >= 0 and j + 1 <= self.y - 1:
            res.append((i-1,j+1))

        self.neighbours[(i, j)] = res

        return

    def sweepObs(self):

        for i in range(10, 21):
            self.obs.append((i, 15))

        for i in range(15):
            self.obs.append((20, i))

        for i in range(15, 30):
            self.obs.append((30, i))

        for i in range(32):
            self.obs.append((40, i))

        return

def main():

    space = Space(100,100)
    space.sweepSpace()
    space.sweepObs()

    gStart = (92,99)
    gEnd  = (30,32)

    aStar = Djisktra(gStart, gEnd, space.neighbours, space.obs)

    path, visited = aStar.search()

    print(path)

if __name__ == '__main__':
    main()