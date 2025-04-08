class Solution:
    def minimumOperations(self, nums):
        operations = 0
        while len(nums) > 0:
            if len(set(nums)) == len(nums):
                break
            nums = nums[3:] if len(nums) >= 3 else []
            operations += 1
        return operations
