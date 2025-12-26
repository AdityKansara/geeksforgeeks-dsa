"""
Problem: Preorder Traversal of Binary Tree
Approach: Depth-First Search (Preorder)
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
    def preOrder(self, root):
        # Helper function to perform preorder traversal
        def traverse(root):
            nodeList = []

            def dfs(node):
                if node is None:
                    return
                nodeList.append(node.data)
                dfs(node.left)
                dfs(node.right)

            dfs(root)
            return nodeList

        # Get preorder traversal result
        result = traverse(root)
        return result
