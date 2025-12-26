"""
Problem: Left View of Binary Tree
Approach: Recursion (DFS) + Track Level
Time Complexity: O(n)
Space Complexity: O(h) due to recursion stack, where h is the height of the tree
"""


# Node class
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def leftView(self, root):
        # Helper function to traverse the tree and collect left view nodes
        def traverse(root) -> list:
            leftv = []

            def dfs(node, level):
                if node is None:
                    return

                # If this is the first node of this level, add it
                if level == len(leftv):
                    leftv.append(node.data)

                # Recur for left and then right child
                dfs(node.left, level + 1)
                dfs(node.right, level + 1)

            dfs(root, 0)
            return leftv

        # Get left view nodes
        lft = traverse(root)
        return lft
