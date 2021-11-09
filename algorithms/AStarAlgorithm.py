from colors import *
from utils import *
import time
from queue import PriorityQueue


def aStarAlgo(grid, speed):
    startNode = get_start_node(grid)
    endNode = get_end_node(grid)

    startNode.distanceFromStart = 0
    startNode.estimatedDistanceToEnd = calculateManhattanDistance(startNode, endNode)
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, startNode))

    open_set_hash = {startNode}

    while not open_set.empty():

        currentNode = open_set.get()[2]
        open_set_hash.remove(currentNode)

        if currentNode == endNode:
            reconstructPath(startNode, endNode)
            return

        for neighbor in getNeighboringNodes(currentNode, grid):
            temp_g_score = currentNode.distanceFromStart + 1

            if temp_g_score < neighbor.distanceFromStart:
                neighbor.cameFrom = currentNode
                neighbor.distanceFromStart = temp_g_score
                heuristic_distance = calculateManhattanDistance(neighbor, endNode)
                neighbor.estimatedDistanceToEnd = temp_g_score + heuristic_distance
                if neighbor not in open_set_hash:
                    if neighbor.color == BLACK:
                        continue
                    count += 1
                    open_set.put((neighbor.estimatedDistanceToEnd, count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.color = GREEN
        if currentNode != startNode:
            currentNode.color = RED
        time.sleep(speed)


def calculateManhattanDistance(currentNode, endNode):
    currentRow = currentNode.row
    currentCol = currentNode.col
    endRow = endNode.row
    endCol = endNode.col
    return abs(currentRow - endRow) + abs(currentCol - endCol)
