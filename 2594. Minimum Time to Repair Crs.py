from typing import List
import math
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left, right = 1, min(ranks) * (cars ** 2)        
        def canRepairInTime(mid):
            total_cars = sum(int(math.sqrt(mid // rank)) for rank in ranks)
            return total_cars >= cars
        while left < right:
            mid = (left + right) // 2
            if canRepairInTime(mid):
                right = mid
            else:
                left = mid + 1
        return left
mintime = Solution()
print(mintime.repairCars([4,2,3,1], 10))
print(mintime.repairCars([5,1,8], 6))
