"""
Problem: Level Order Traversal
Approach: Breadth-First Search (BFS) using a queue.
          Traverse the tree level by level, processing all nodes
          at the current level before moving to the next.
Time Complexity: O(n) - each node is visited once
Space Complexity: O(n) - queue stores nodes at each level
"""

import collections


class Solution:
    def levelOrder(self, root):
        if root is None:
            return []

        result = []
        q = collections.deque([root])

        while q:
            level = []
            level_size = len(q)

            for _ in range(level_size):
                node = q.popleft()
                level.append(node.data)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(level)

        return result
