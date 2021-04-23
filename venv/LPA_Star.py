import heapq
import math

class AStar:

    def __init__(self, gStart, gEnd, neighbours, obs):

        self.gStart = gStart
        self.gEnd = gEnd
        self.neighbours = neighbours
        self.obs = obs
        self.gMap = {}
        self.rhs = {}
        self.heap = []
        self.parent = {}
        self.visited = []

    def search(self):

        self.gMap[self.gStart] = math.inf
        self.rhs[self.gStart] = 0
        self.parent[self.gStart] = self.gStart

        heapq.heappush(self.heap, (self.fFunc1(self.gStart), self.fFunc2(self.gStart), self.gStart))

        self.visited.append(self.gStart)

        while len(self.heap) is not 0:

            currEle = self.heap[0]
            currPos = currEle[2]

            self.visited.append(currPos)

            if self.rhs[self.gEnd] == self.gMap[self.gEnd] and (currEle[0], currEle[1]) >= (self.fFunc1(self.gEnd), self.fFunc2(self.gEnd)):
                break

            if self.rhs[currPos] < self.gMap[currPos]:
                self.gMap[currPos] = self.rhs[currPos]
            else:
                self.gMap[currPos] = math.inf


            for neighbour in self.neighbours[currPos]:
                self.estRHS(neighbour)


        return self.printPath()

    def fFunc1(self, currPos):

        return min(self.gMap[currPos], self.rhs[currPos]) + ((self.gEnd[0] - currPos[0])^2 + (self.gEnd[1] - currPos[1])^2)

    def fFunc2(self, currPos):

        return min(self.gMap[currPos], self.rhs[currPos])

    def cost(self, currPos, neighbour):

        if neighbour in self.obs:
            return math.inf

        return 10

    def estRHS(self, curr):

        self.rhs[curr] = math.inf

        for neighbour in self.neighbours[curr]:
            self.rhs[curr] = min(self.gMap[neighbour] + self.cost(neighbour, curr), self.rhs[curr])

        #if self.rhs[curr] == self.gMap[curr]:
            heapq.heappop(self.heap)

        if self.rhs[curr] != self.gMap[curr]:
            heapq.heappush(self.heap, (self.fFunc1(curr), self.fFunc2(curr), curr))

        return

    def printPath(self):

        path = []
        currPos = self.gEnd
        path.append(currPos)

        while True:
            minCostMap = {}

            for neighbour in self.neighbours[currPos]:
                minCostMap[neighbour] = self.gMap[neighbour] + self.cost(neighbour, curr)

            path.append(min(minCostMap, key=minCostMap.get))

            currPos = min(minCostMap, key=minCostMap.get)

            if currPos == self.gStart:
                path.append(currPos)
                break

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

    aStar = AStar(gStart, gEnd, space.neighbours, space.obs)

    path, visited = aStar.search()

    print(path)

if __name__ == '__main__':
    main()