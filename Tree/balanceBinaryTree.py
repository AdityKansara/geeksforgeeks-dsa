"""
Problem: Check if Binary Tree is Height Balanced
Approach: Recursive height calculation + balance check.
          For each node, calculate heights of left and right subtrees
          and ensure their difference is not more than 1.
Time Complexity: O(n^2) in worst case (repeated height calculations)
Space Complexity: O(h) - recursion stack, where h is the height of the tree
"""

class Solution:
    def isBalanced(self, root):

        def heightCheck(rt):
            if rt == None:
                return 0

            return 1 + max(heightCheck(rt.right), heightCheck(rt.left))

        # An empty tree is balanced
        if root == None:
            return True

        # Calculate heights of left and right subtrees
        rHeight = heightCheck(root.right)
        lHeight = heightCheck(root.left)

        # If height difference is more than 1, tree is not balanced
        if abs(rHeight - lHeight) > 1:
            return False

        # Recursively check balance of left and right subtrees
        l = self.isBalanced(root.left)
        r = self.isBalanced(root.right)

        if not l or not r:
            return False

        return True
