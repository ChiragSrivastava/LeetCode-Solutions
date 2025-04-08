from collections import Counter

class Solution:
    def maxOperations(self, nums, k):
        count = Counter(nums)
        operations = 0
        for num in nums:
            complement = k - num
            if count[num] > 0 and count[complement] > 0:
                if num == complement and count[num] >= 2:
                    count[num] -= 2
                    operations += 1
                elif num != complement:
                    count[num] -= 1
                    count[complement] -= 1
                    operations += 1
        return operations
