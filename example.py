from GraphAlgorithm import *
from CreateRandomGraph import *

graph = constructGraph()
ax = graph.getFigure()
# define the start and end id of shortest path want to calculate.
start, end = 1, 19
GA = GraphAlgorithm()
graph = GA.shortestPath(graph, start, end, "a*")
shortestPath = graph.vertexes[end].sp
# draw the shortest path on the existing graph.
ax = GA.showShortestPath(graph, shortestPath)
# save figure to the given path
os.makedirs(figSavePath,exist_ok=True)
ax.figure.savefig(figSavePath + "result.png")

