from colors import *
import time
from queue import PriorityQueue


def dijkstraAlgo(grid):
    visited = {node: False for row in grid for node in row}
    startNode = get_start_node(grid)
    endNode = get_end_node(grid)
    startNode.distanceFromStart = 0
    priority_queue = PriorityQueue()
    priority_queue.put((0, startNode))
    while not priority_queue.empty():
        current = priority_queue.get()[1]
        time.sleep(0.01)
        if visited[current]:
            continue
        visited[current] = True
        if current == endNode:
            reconstructPath(startNode, endNode)
            return
        if current != startNode:
            current.color = RED
        for neighbor in getNeighboringNodes(current, grid):
            if neighbor.color == BLACK:
                continue
            if current.distanceFromStart + 1 < neighbor.distanceFromStart:
                neighbor.cameFrom = current
                neighbor.distanceFromStart = current.distanceFromStart + 1
                priority_queue.put((neighbor.distanceFromStart, neighbor))
            if neighbor != endNode and neighbor != startNode and not visited[neighbor]:
                neighbor.color = GREEN


def flattenGrid(grid):
    return [node for rows in grid for node in rows]


def updateUnvisitedNeighbors(node, grid):
    unvisitedNeighbors = getNeighboringNodes(node, grid)
    for neighbor in unvisitedNeighbors:
        neighbor.distanceFromStart = node.distanceFromStart + 1
        neighbor.cameFrom = node


def reconstructPath(startNode, endNode):
    if not endNode.cameFrom:
        return

    currentNode = endNode
    while currentNode:
        currentNode.color = PURPLE
        currentNode = currentNode.cameFrom
        time.sleep(0.01)

    startNode.color = BLUE
    endNode.color = BROWN


def getNeighboringNodes(node, nodes):
    neighbors = []

    numRows = len(nodes)
    numCols = len(nodes[0])

    row = node.row
    col = node.col

    if row < numRows - 1:
        neighbors.append(nodes[row + 1][col])
    if row > 0:
        neighbors.append(nodes[row - 1][col])
    if col < numCols - 1:
        neighbors.append(nodes[row][col + 1])
    if col > 0:
        neighbors.append(nodes[row][col - 1])
    return neighbors


def sortNodesByDistance(unvisitedNodes):
    unvisitedNodes.sort(key=lambda node: node.distanceFromStart)
    print(unvisitedNodes[0].distanceFromStart, "first node")
    print(unvisitedNodes[20].distanceFromStart, "second node")
    print(unvisitedNodes[-1].distanceFromStart, "last node")


def get_start_node(grid):
    for row in grid:
        for node in row:
            if node.isStart == True:
                return node


def get_end_node(grid):
    for row in grid:
        for node in row:
            if node.isEnd == True:
                return node
