from collections import defaultdict

class Solution:
    def countBadPairs(self, nums):
        freq = defaultdict(int)
        n = len(nums)
        total_pairs = (n * (n - 1)) // 2 
        good_pairs = 0  

        for i, num in enumerate(nums):
            key = num - i 
            good_pairs += freq[key] 
            freq[key] += 1 

        return total_pairs - good_pairs 
