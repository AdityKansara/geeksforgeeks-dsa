"""
Problem: Height of Binary Tree
Approach: Recursion (Bottom-up)
Time Complexity: O(n)
Space Complexity: O(h) where h is the height of the tree (due to recursion stack)
"""


# Node class
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def height(self, root):
        # Base case: empty tree has height -1
        if root is None:
            return -1

        # Recursively find height of left and right subtrees
        lftHeight = self.height(root.left)
        rtHeight = self.height(root.right)

        # Height of current node = 1 + max of left and right subtree heights
        return 1 + max(lftHeight, rtHeight)
