"""
Problem: Inorder Traversal of Binary Tree
Approach: Depth-First Search (Inorder)
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
    def inOrder(self, root):
        # Helper function to perform inorder traversal
        def traverse(root):
            nodelist = []

            def dfs(node):
                if node is None:
                    return
                dfs(node.left)
                nodelist.append(node.data)
                dfs(node.right)

            dfs(root)
            return nodelist

        # Get inorder traversal result
        result = traverse(root)
        return result
