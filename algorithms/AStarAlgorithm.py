from colors import *
import time
from queue import PriorityQueue


def aStarAlgo(grid):
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
        time.sleep(0.0001)


def calculateManhattanDistance(currentNode, endNode):
    currentRow = currentNode.row
    currentCol = currentNode.col
    endRow = endNode.row
    endCol = endNode.col
    return abs(currentRow - endRow) + abs(currentCol - endCol)


class MinHeap:
    def __init__(self, array):
        self.nodePositionsInHeap = {node.idx: idx for idx, node in enumerate(array)}
        self.heap = self.buildHeap(array)

    def isEmpty(self):
        return len(self.heap) == 0

    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = childOneIdx + 1 if childOneIdx + 1 <= endIdx else -1
            if (
                childTwoIdx != None
                and heap[childTwoIdx].estimatedDistanceToEnd
                < heap[childOneIdx].estimatedDistanceToEnd
            ):
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if (
                heap[idxToSwap].estimatedDistanceToEnd
                < heap[currentIdx].estimatedDistanceToEnd
            ):
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return

    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while (
            currentIdx > 0
            and heap[currentIdx].estimatedDistanceToEnd
            < heap[parentIdx].estimatedDistanceToEnd
        ):
            self.swap(currentIdx, parentIdx, heap)

    def remove(self):
        if self.isEmpty():
            return

        self.swap(0, len(self.heap) - 1, self.heap)
        node = self.heap.pop()
        del self.nodePositionsInHeap[node.idx]
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return node

    def insert(self, node):
        self.heap.append(node)
        self.nodePositionsInHeap[node.idx] = len(self.heap) - 1
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        self.nodePositionsInHeap[heap[i].idx] = j
        self.nodePositionsInHeap[heap[j].idx] = i
        heap[i], heap[j] = heap[j], heap[i]

    def containsNode(self, node):
        return node.idx in self.nodePositionsInHeap

    def update(self, node):
        self.siftUp(self.nodePositionsInHeap[node.idx], self.heap)


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
