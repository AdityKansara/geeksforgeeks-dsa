"""
Problem: Binary Search - Find First (Smallest) Occurrence
Approach: Modified binary search; when the target is found, record the index and continue searching in the left half to find an earlier occurrence
Time Complexity: O(log n) - binary search with continued halving
Space Complexity: O(1) - constant extra space
Created by AdityKansara
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


if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 5]
    target = 2
    print(f"First occurrence of {target}: {binarySearch(arr, target)}")
