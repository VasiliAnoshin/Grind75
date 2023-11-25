"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def clone(node):
            if not node:
                return        
            new_node = Node(node.val, [])
            exist[node.val] = new_node
            for neighbor in node.neighbors:
                if neighbor.val not in exist:
                    clone(neighbor)
                exist[new_node.val].neighbors.append(exist[neighbor.val])
            return new_node
        exist = dict()
        return clone(node)