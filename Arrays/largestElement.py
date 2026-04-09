"""
Problem: Find the largest element in an array of integers.
Approach: Scan through the list and keep track of the maximum value seen so far.
Time Complexity: O(n) - single pass through the array
Space Complexity: O(1) - constant extra space
Created by AdityKansara
"""

class Solution:
    def largestElement(self, nums):
        max_value = -100000

        for i in nums:
            if i > max_value:
                max_value = i
        return max_value

if __name__ == "__main__":
    nums = [3, 7, 2, 9, 5]
    result = Solution().largestElement(nums)
    print(f"Largest element: {result}")