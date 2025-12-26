"""
Problem: Postorder Traversal of Binary Tree
Approach: Depth-First Search (Postorder)
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
    def postOrder(self, root):
        # Helper function to perform postorder traversal
        def traverse(root):
            nodeList = []

            def dfs(node):
                if node is None:
                    return
                dfs(node.left)
                dfs(node.right)
                nodeList.append(node.data)

            dfs(root)
            return nodeList

        # Get postorder traversal result
        result = traverse(root)
        return result
