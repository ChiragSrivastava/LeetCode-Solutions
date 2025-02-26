from typing import List

class Solution:
    def maxAbsoluteSum(self, x: List[int]) -> int:
        max_sum = min_sum = max_so_far = min_so_far = 0        
        for me in x:
            max_so_far = max(me, max_so_far + me)
            max_sum = max(max_sum, max_so_far)
            min_so_far = min(me, min_so_far + me)
            min_sum = min(min_sum, min_so_far)
        return max(max_sum, abs(min_sum))
