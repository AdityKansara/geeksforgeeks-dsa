"""
Problem: Sum of All Nodes in a Binary Tree
Approach: Recursion (DFS)
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
    # Function to return sum of all nodes in a binary tree
    def sumBT(self, root):
        # Helper function: returns sum of nodes in the subtree rooted at 'root'
        def dfs(node):
            if node is None:
                return 0
            return node.data + dfs(node.left) + dfs(node.right)

        return dfs(root)
