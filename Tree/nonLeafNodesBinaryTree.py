"""
Problem: Count Non-Leaf Nodes in a Binary Tree
Approach: Recursion (DFS, return-based)
Time Complexity: O(n) - each node is visited once
Space Complexity: O(h) - recursion stack, where h is the height of the tree
"""


# Node class
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    # Function to count the number of non-leaf nodes in a binary tree
    def countNonLeafNodes(self, root):
        # Helper function: returns number of non-leaf nodes in the subtree rooted at 'root'
        def dfs(node):
            if node is None:
                return 0
            # If node has at least one child, it's a non-leaf
            if node.left or node.right:
                return 1 + dfs(node.left) + dfs(node.right)
            # Leaf node contributes 0
            return 0

        return dfs(root)
