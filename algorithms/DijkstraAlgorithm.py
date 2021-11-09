from colors import *
from utils import *
import time
from queue import PriorityQueue


def dijkstraAlgo(grid, speed):
    visited = {node: False for row in grid for node in row}
    startNode = get_start_node(grid)
    endNode = get_end_node(grid)
    startNode.distanceFromStart = 0
    priority_queue = PriorityQueue()
    priority_queue.put((0, startNode))
    while not priority_queue.empty():
        current = priority_queue.get()[1]
        time.sleep(speed / 10)
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
