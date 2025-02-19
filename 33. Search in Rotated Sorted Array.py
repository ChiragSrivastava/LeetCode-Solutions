from typing import List

class Solution:
    def search(self, a: List[int], target: int) -> int:
        left, right = 0, len(a) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if a[mid] == target:
                return mid 
            if a[left] <= a[mid]:
                if a[left] <= target < a[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if a[mid] < target <= a[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1
rotating_array = Solution()
print(rotating_array.search([4,5,6,7,0,1,2], 0))
print(rotating_array.search([4,5,6,7,0,1,2], 3))
print(rotating_array.search([1], 0))
