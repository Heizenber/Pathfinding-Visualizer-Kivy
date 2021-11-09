from colors import *
import time


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
