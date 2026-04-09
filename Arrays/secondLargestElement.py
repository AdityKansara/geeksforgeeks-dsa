"""
Problem: Find the second largest unique element in an array of integers.
Approach: Track the largest and second largest values in one pass while ignoring duplicates.
Time Complexity: O(n) - single pass through the list
Space Complexity: O(1) - constant extra space
Created by AdityKansara
"""

class Solution:
    def secondLargestElement(self, nums):
        largest = float('-inf')
        slargest = float('-inf')

        for i in nums:
            if i > largest:
                slargest = largest
                largest = i
            elif i < largest and i > slargest:
                slargest = i
        if slargest == float('-inf'):
            return -1
        return slargest

if __name__ == "__main__":
    nums = [10, 5, 20, 20, 4, 5]
    result = Solution().secondLargestElement(nums)
    print(f"Second largest element: {result}")