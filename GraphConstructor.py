import matplotlib.pyplot as plt

from Config import *

class Point:
    def __init__(self, id, coordinate):
        self.id = id
        self.coordinate = coordinate

    def cal_dist(self, v):
        return np.sqrt(np.sum(np.square(self.coordinate - v.coordinate)))


class Vertex(Point):
    def __init__(self, id, coordinate):
        self.id = id
        self.coordinate = coordinate
        self.distance = np.inf
        self.loss = np.inf
        self.sp = [id]



class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight


class Graph:
    def __init__(self, vertexes, edgeList):
        self.vertexes = vertexes
        self.edgeList = edgeList
        self.pointsNum = len(vertexes)

    def resetGraph(self):
        for i in range(self.vertexes):
            self.vertexes[i].distance = np.inf
            self.vertexes[i].loss = np.inf
            self.vertexes[i].sp = [self.vertexes[i].id]

    def getFigure(self):
        fig, ax = plt.subplots()
        for i, vertex in enumerate(self.vertexes):
            ax.scatter(vertex.coordinate[0], vertex.coordinate[1], c='r')
            ax.annotate(i, vertex.coordinate)

        for i, adjEdges in enumerate(self.edgeList):
            for j, adjEdge in enumerate(adjEdges):
                x1, y1 = self.vertexes[adjEdge.start].coordinate
                x2, y2 = self.vertexes[adjEdge.end].coordinate
                ax.plot([x1, x2], [y1, y2], c='b')

        return ax

    def getAdjMat(self):

        mat = np.zeros((self.pointsNum, self.pointsNum))
        for i in range(self.pointsNum):
            for edge in self.edgeList[i]:
                mat[i, edge.end] += 1
        return mat
