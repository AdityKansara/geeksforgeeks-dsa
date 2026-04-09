"""
Problem: Find the index of a target value in an array using linear search.
Approach: Iterate through the array until the target is found, then return the index.
Time Complexity: O(n) - scan through the list until the item is found or end is reached
Space Complexity: O(1) - constant extra space
Created by AdityKansara
"""

class Solution:
    def linearSearch(self, nums, target):
        for i,val in enumerate(nums):
            if val == target:
                return i
        return -1

if __name__ == "__main__":
    nums = [4, 2, 7, 1, 3]
    target = 7
    result = Solution().linearSearch(nums, target)
    print(f"Target {target} found at index: {result}")