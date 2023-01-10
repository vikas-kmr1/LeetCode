"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# Time: O(V + E) - for DFS
# Space: O(V) - for the hashmap

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        cloneMap =dict()
        
        def clone(node):
            if node in cloneMap:
                return cloneMap.get(node)
            
            cloneNode = Node(node.val)
            cloneMap[node] = cloneNode
            
            for neighbor in node.neighbors:
                cloneNode.neighbors.append(clone(neighbor))
            return cloneNode
        
        return clone(node) if node else None
            
        