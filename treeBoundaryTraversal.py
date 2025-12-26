"""
Problem: Boundary Traversal of Binary Tree
Platform: GeeksforGeeks
Approach: DFS Traversal (Left boundary, Leaf nodes, Right boundary)
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
    def boundaryTraversal(self, root):
        # Helper function to get boundary nodes
        def traverse(root) -> list:
            nodelist = []
            tmp = []

            # Traverse the left boundary (excluding leaves)
            def lft(node):
                if node is None:
                    return
                if node.left:
                    if not (node.left is None and node.right is None):
                        nodelist.append(node.data)
                        lft(node.left)
                elif node.right:
                    if not (node.left is None and node.right is None):
                        nodelist.append(node.data)
                        lft(node.right)

            # Traverse all leaf nodes
            def leaf(node):
                if node.left is None and node.right is None:
                    nodelist.append(node.data)
                else:
                    if node.left:
                        leaf(node.left)
                    if node.right:
                        leaf(node.right)

            # Traverse the right boundary (excluding leaves)
            def rt(node) -> list:
                if node is None:
                    return
                if node.right:
                    tmp.append(node.data)
                    rt(node.right)
                elif node.left:
                    tmp.append(node.data)
                    rt(node.left)
                return tmp

            # Add root node
            if root is not None:
                nodelist.append(root.data)

            # Add left boundary
            if root.left:
                lft(root.left)

            # Add leaf nodes
            if not (root.left is None and root.right is None):
                leaf(root)

            # Add right boundary in reverse
            if root.right:
                tmp = rt(root.right)
            for i in range(len(tmp)):
                nodelist.append(tmp[len(tmp) - i - 1])

            return nodelist

        # Get all boundary nodes
        nodes = traverse(root)
        return nodes
