class Solution:
    def maxAscendingSum(self, a):
        max_sum = curr_sum = a[0]
        
        for i in range(1, len(a)):
            if a[i] > a[i - 1]: 
                curr_sum += a[i]
            else: 
                max_sum = max(max_sum, curr_sum)
                curr_sum = a[i]
        
        return max(max_sum, curr_sum)  


ArraySum = Solution()
print(ArraySum.maxAscendingSum([10, 20, 30, 5, 10, 50]))
print(ArraySum.maxAscendingSum([10, 20, 30, 40, 50]))
print(ArraySum.maxAscendingSum([12, 17, 15, 13, 10, 11, 12]))
