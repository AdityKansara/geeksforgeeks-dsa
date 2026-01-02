"""
Problem: Book Allocation (Allocate Minimum Number of Pages)
Approach: Binary search on the answer with a greedy feasibility check.
          For a given maximum page limit, determine how many students
          are required if books are allocated contiguously.
Time Complexity: O(n log(sum(arr))) – binary search with linear check
Space Complexity: O(1) – constant extra space
"""


def findPages(arr, k):
    # Helper function to calculate number of students required
    # if no student is allowed to read more than max_pages
    def required_students(max_pages):
        students = 1  # At least one student
        pages_allocated = 0  # Pages allocated to current student

        for pages in arr:
            if pages_allocated + pages <= max_pages:
                pages_allocated += pages
            else:
                students += 1
                pages_allocated = pages

        return students

    # Impossible case: fewer books than students
    if len(arr) < k:
        return -1

    # Search space for binary search
    low = max(arr)  # Minimum possible maximum pages
    high = sum(arr)  # Maximum possible maximum pages

    # Binary search on the answer
    while low <= high:
        mid = (low + high) // 2

        if required_students(mid) > k:
            # Too many students needed → increase page limit
            low = mid + 1
        else:
            # Valid allocation → try to minimize further
            high = mid - 1

    return low


# Example usage
if __name__ == "__main__":
    print(findPages([12, 34, 67, 90], 2))  # Output: 113
