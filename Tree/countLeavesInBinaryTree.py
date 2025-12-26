"""
Problem: Count Leaf Nodes in a Binary Tree
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
    # Function to count the number of leaf nodes in a binary tree
    def countLeaves(self, root):
        # Helper function: returns number of leaves in the subtree rooted at 'root'
        def dfs(node):
            if node is None:
                return 0
            if not node.left and not node.right:
                return 1
            return dfs(node.left) + dfs(node.right)

        return dfs(root)
