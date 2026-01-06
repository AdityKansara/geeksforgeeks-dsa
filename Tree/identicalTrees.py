"""
Problem: Check if Two Trees are Identical
Approach: Recursive DFS comparison.
          At each step, compare current nodes and
          recursively check left and right subtrees.
Time Complexity: O(n) - each node is visited once
Space Complexity: O(h) - recursion stack, where h is the height of the tree
"""


class Solution:
    def isIdentical(self, r1, r2):
        # Helper function to compare two trees
        def dfs(root1, root2):
            # Case 1: both nodes are None
            if root1 is None and root2 is None:
                return True

            # Case 2: one node is None and the other is not
            if root1 is None or root2 is None:
                return False

            # Case 3: data mismatch
            if root1.data != root2.data:
                return False

            # Case 4: compare left and right subtrees
            return dfs(root1.left, root2.left) and dfs(root1.right, root2.right)

        return dfs(r1, r2)
