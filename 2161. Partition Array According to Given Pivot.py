from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left, middle, right = [], [], []        
        for num in nums:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                middle.append(num)        
        return left + middle + right
pivot_array = Solution()
print(pivot_array.pivotArray([9,12,5,10,14,3,10], 10))
print(pivot_array.pivotArray([-3,4,3,2], 2))
