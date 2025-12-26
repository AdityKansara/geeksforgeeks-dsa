"""
Problem: Size of a Binary Tree
Approach: Recursion (DFS)
Time Complexity: O(n) - each node is visited once
Space Complexity: O(h) - recursion stack, where h is the height of the tree
"""

from typing import Optional


# Node class
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    # Function to return the size (number of nodes) of the binary tree
    def getSize(self, node: Optional["Node"]) -> int:
        # Helper function: returns number of nodes in the subtree rooted at 'root'
        def dfs(root):
            if root is None:
                return 0
            return 1 + dfs(root.left) + dfs(root.right)

        return dfs(node)
