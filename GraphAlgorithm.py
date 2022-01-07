from Config import *


class GraphAlgorithm:
    def __init__(self):
        ...

    def priorityQueue(self, currentPointList, graph):
        # 存储权重最小的点，作为下一次循环的遍历节点
        min_loss = np.inf
        for j, point in enumerate(currentPointList):
            if graph.vertexes[point].loss < min_loss:
                min_loss = graph.vertexes[point].loss
                min_index = point

        currentPointList.remove(min_index)
        return [min_index] + currentPointList

    def shortestPath(self, graph, start, end, method = "dijkstra"):
        graph.vertexes[start].loss, graph.vertexes[start].distance = 0, 0
        visited = []
        currentPointList = [start]
        step_count = 0
        while True:
            # 获取当前点集中距离权重最小的进行广度遍历搜索
            point = currentPointList.pop(0)
            visited.append(point)
            adjEdge = graph.edgeList[point]
            adjPoints = [edge.end for edge in adjEdge]

            for j, adjPoint in enumerate(adjPoints):
                if adjPoint not in visited and adjPoint not in currentPointList:
                    currentPointList.append(adjPoint)
                new_dist = adjEdge[j].weight + graph.vertexes[point].distance
                if method == "dijkstra":
                    new_loss = new_dist
                elif method == "a*":
                    new_loss = new_dist + graph.vertexes[adjPoint].cal_dist(graph.vertexes[end])
                else:
                    print("方法输入错误")
                    return

                if new_dist < graph.vertexes[adjPoint].distance:
                    graph.vertexes[adjPoint].sp = graph.vertexes[point].sp + [adjPoint]
                    graph.vertexes[adjPoint].loss = new_loss
                    graph.vertexes[adjPoint].distance = new_dist

            currentPointList = self.priorityQueue(currentPointList, graph)
            if currentPointList[0] == end:
                break
            step_count += 1

        print("最短路搜索花费步数：", step_count)
        return graph

    def showShortestPath(self, graph, shortestPath):
        ax = graph.getFigure()

        for i in range(len(shortestPath)-1):
            x1, y1 = graph.vertexes[shortestPath[i]].coordinate
            x2, y2 = graph.vertexes[shortestPath[i+1]].coordinate
            ax.plot([x1,x2], [y1,y2], c='g')
        return ax
