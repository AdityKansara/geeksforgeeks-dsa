"""
Problem: Find Maximum and Minimum Node Values in a Binary Tree
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
    # -----------------------------
    # Find Maximum Node Value
    # -----------------------------
    # Approach 1: Direct simple recursion
    # Safe for any integer values, returns maximum in subtree
    def findMax(self, root):
        if root is None:
            return float(
                "-inf"
            )  # use -inf instead of 0 for safety with negative values
        return max(root.data, self.findMax(root.left), self.findMax(root.right))

    # Approach 2: Using DFS helper with intermediate variables
    # Keeps track of current node and compares with left and right recursively
    def findMinDFS(self, root):
        def dfs(node):
            if node is None:
                return float("inf")
            currentMin = node.data
            leftMin = min(dfs(node.left), currentMin)
            rightMin = min(dfs(node.right), currentMin)
            return min(leftMin, rightMin)

        return dfs(root)
