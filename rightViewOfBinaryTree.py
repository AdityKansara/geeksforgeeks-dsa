"""
Problem: Right View of Binary Tree
Approach: Recursion (DFS) + Track Level (Right-first)
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
    def rightView(self, root):
        # Helper function to collect right view nodes
        def traverse(root):
            rightView = []

            def rightdfs(node, level):
                if node is None:
                    return

                # If this is the first node at this level, add it
                if level == len(rightView):
                    rightView.append(node.data)

                # Visit right child first, then left child
                rightdfs(node.right, level + 1)
                rightdfs(node.left, level + 1)

            rightdfs(root, 0)
            return rightView

        # Get right view nodes
        result = traverse(root)
        return result
