from colors import *


def dijkstraAlgo():
    pass


# def dijkstrasAlgorithm(start, edges):
#     # Write your code here.
#     numberOfEdges = len(edges)
# 	minDistances = [float('inf') for _ in range(numberOfEdges)]
# 	minDistances[start] = 0
# 	visited = set()

# 	while len(visited) != numberOfEdges:
# 		vertex, currentMinDistance = getVertexWithDistance(minDistances, visited)

# 		if currentMinDistance == float('inf'):
# 			break

# 		visited.add(vertex)

# 		for edge in edges[vertex]:
# 			destination, distanceToDestination = edge

# 			newPathDistance = distanceToDestination + currentMinDistance
# 			currentMinDistanceToDestination = minDistances[destination]
# 			if newPathDistance < currentMinDistanceToDestination:
# 				minDistances[destination] = newPathDistance
# 	return list(map(lambda x: -1 if x == float('inf') else x, minDistances))


# def getVertexWithDistance(distances, visited):
# 	vertex = None
# 	currentMinDistance = float('inf')

# 	for vertexIdx, distance in enumerate(distances):
# 		if vertexIdx in visited:
# 			continue

# 		if distance <= currentMinDistance:
# 			currentMinDistance = distance
# 			vertex = vertexIdx
# 	return vertex, currentMinDistance
