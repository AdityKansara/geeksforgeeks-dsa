"""
Problem: Binary Search - Find First (Smallest) Occurrence
Approach: Modified binary search; when the target is found, record the index and continue searching in the left half to find an earlier occurrence
Time Complexity: O(log n) - binary search with continued halving
Space Complexity: O(1) - constant extra space
"""


def binarySearch(arr, k):
    l = 0
    r = len(arr) - 1
    result = -1

    while l <= r:
        m = (l + r) // 2

        if arr[m] == k:
            result = m  # store potential answer
            r = m - 1  # move left to find smaller index
        elif arr[m] > k:
            r = m - 1
        else:
            l = m + 1

    return result
