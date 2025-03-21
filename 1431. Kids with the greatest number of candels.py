from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [(candy + extraCandies) >= max_candies for candy in candies]
length = Solution()
print(length.kidsWithCandies([2,3,5,1,3], 3))
print(length.kidsWithCandies([4,2,1,1,2], 1))
print(length.kidsWithCandies([12,1,12], 10))
