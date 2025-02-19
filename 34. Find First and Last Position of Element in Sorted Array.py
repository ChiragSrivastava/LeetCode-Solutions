from typing import List

class Solution:
    def searchRange(self, a: List[int], target: int) -> List[int]:
        def findFirst(a, target):
            left, right = 0, len(a) - 1
            first = -1
            while left <= right:
                mid = (left + right) // 2
                if a[mid] == target:
                    first = mid
                    right = mid - 1
                elif a[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return first

        def findLast(a, target):
            left, right = 0, len(a) - 1
            last = -1
            while left <= right:
                mid = (left + right) // 2
                if a[mid] == target:
                    last = mid
                    left = mid + 1
                elif a[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return last

        first = findFirst(a, target)
        last = findLast(a, target)
        return [first, last]

sort_array = Solution()
print(sort_array.searchRange([5,7,7,8,8,10], 8))
print(sort_array.searchRange([5,7,7,8,8,10], 6))
print(sort_array.searchRange([], 0))
