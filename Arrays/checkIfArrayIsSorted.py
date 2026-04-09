"""
Problem: Check if array is sorted in non-decreasing order.
Approach: Iterate through the list and verify each value is greater than or equal to the previous one.
Time Complexity: O(n) - single pass through the array
Space Complexity: O(1) - constant extra space
Created by AdityKansara
"""

class Solution:
    def isSorted(self, nums):
        previous = float('-inf')

        for i in nums:
            if i < previous:
                return False
            previous = i
        return True

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    result = Solution().isSorted(nums)
    print(f"Array is sorted: {result}")