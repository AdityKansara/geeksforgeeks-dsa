"""
Problem: Sum of Leaf Nodes in a Binary Tree
Platform: GeeksforGeeks
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
    # Function to return the sum of all leaf nodes in a binary tree
    def leafSum(self, root):
        if root is None:
            return 0
        # If node is a leaf, return its value
        if not root.left and not root.right:
            return root.data
        # Otherwise, sum leaf nodes from left and right subtrees
        return self.leafSum(root.left) + self.leafSum(root.right)
