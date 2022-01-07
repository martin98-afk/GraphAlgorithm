from Config import *
from GraphConstructor import *

def getDistanceMat(vertexes, k = 5):
    pointsNum = len(vertexes)
    mat = np.zeros((pointsNum, pointsNum))
    for i in range(pointsNum):
        for j in range(i+1, pointsNum):
            mat[i, j] = vertexes[i].cal_dist(vertexes[j])
            mat[j, i] = vertexes[i].cal_dist(vertexes[j])

    adjMat = np.zeros_like(mat)
    for i in range(pointsNum):
        seq = list(np.argsort(mat[i,:])[:k])
        seq.pop(0)
        for index in seq:
            adjMat[i, index] = 1

    return mat, adjMat

def constructGraph():
    # construct graph
    vertexes = [Vertex(id, np.array([np.random.random(), np.random.random()])) for id in
                range(20)]
    mat, adjMat = getDistanceMat(vertexes)
    edges = [[] for i in range(20)]
    for i in range(20):
        seq = np.where(adjMat[i, :] != 0)[0]
        for j in seq:
            edges[i].append(Edge(i, j, mat[i,j]))

    graph = Graph(vertexes, edges)
    return graph