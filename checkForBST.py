"""
Problem: Check if Binary Tree is a BST
Approach: Inorder Traversal + Array Check
Time Complexity: O(n)
Space Complexity: O(n) for storing inorder traversal
"""

# Node class
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def isBST(self, root):
        # Helper function to perform inorder traversal
        def traverse(root) -> list:
            nodelist = []

            def dfs(node):
                if node is None:
                    return
                dfs(node.left)
                nodelist.append(node.data)
                dfs(node.right)

            dfs(root)
            return nodelist

        # Get inorder traversal of tree
        nodes = traverse(root)

        # Check if the inorder traversal is strictly increasing
        for i, val in enumerate(nodes):
            if i < len(nodes) - 1:
                if nodes[i] >= nodes[i + 1]:
                    return False

        return True
