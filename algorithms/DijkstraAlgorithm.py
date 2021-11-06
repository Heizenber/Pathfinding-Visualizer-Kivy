from colors import *


def dijkstraAlgo(grid):
    numberOfNodes = len(grid)
    startNode = get_start_node(grid)
    minDistances = [float("inf") for _ in range(numberOfNodes)]
    minDistances[startNode] = 0
    visited = set()

    while len(visited) != numberOfNodes:
        vertex, currentMinDistance = getVertexWithDistance(minDistances, visited)

        if currentMinDistance == float("inf"):
            break

        visited.add(vertex)

        for edge in grid[vertex]:
            destination, distanceToDestination = edge

            newPathDistance = distanceToDestination + currentMinDistance
            currentMinDistanceToDestination = minDistances[destination]
            if newPathDistance < currentMinDistanceToDestination:
                minDistances[destination] = newPathDistance
    return list(map(lambda x: -1 if x == float("inf") else x, minDistances))


def getVertexWithDistance(distances, visited):
    vertex = None
    currentMinDistance = float("inf")

    for vertexIdx, distance in enumerate(distances):
        if vertexIdx in visited:
            continue

        if distance <= currentMinDistance:
            currentMinDistance = distance
            vertex = vertexIdx
    return vertex, currentMinDistance


def get_start_node(grid):
    for row in grid:
        for node in row:
            if node.isStart == True:
                return node
