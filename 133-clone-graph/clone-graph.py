"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None


        start=node
        stk=[start]
        visited=set()
        o_to_n={}
        visited.add(start)

        while stk:
            node=stk.pop()
            o_to_n[node]=Node(val=node.val)

            for n in node.neighbors:
                if n not in visited:
                    visited.add(n)
                    stk.append(n)
        for old_new,  new_node in o_to_n.items():
            for n in old_new.neighbors:
                new_node.neighbors.append(o_to_n[n])
        
        return o_to_n[start]


    
        




        