"""
Problem: Left rotate an array by one position.
Approach: Save the first element, shift all elements one position to the left,
then place the saved element at the end of the array.
Time Complexity: O(n) - each element is moved once
Space Complexity: O(1) - constant extra space
Created by AdityKansara
"""

class Solution:
    def rotateArrayByOne(self, nums):
        if not nums:
            return nums

        first = nums[0]
        l = len(nums)
        for i in range(l - 1):
            nums[i] = nums[i + 1]
        nums[l - 1] = first

        return nums

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    result = Solution().rotateArrayByOne(nums)
    print(f"Rotated array: {result}")