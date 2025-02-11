class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num  
        return result

linear = Solution()
print(linear.singleNumber([2, 2, 1]))
print(linear.singleNumber([4, 1, 2, 1, 2]))
print(linear.singleNumber([1]))
