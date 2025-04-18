from typing import List
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left, right = min(nums), max(nums) 
        def canRob(cap):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= cap:
                    count += 1
                    i += 1
                i += 1
            return count >= k
        while left < right:
            mid = (left + right) // 2
            if canRob(mid):
                right = mid
            else:
                left = mid + 1
        return left
house = Solution()
print(house.minCapability([2,3,5,9], 2))
print(house.minCapability([2,7,9,3,1], 2))
