class Solution:
    def grayCode(self, n):
        return [i ^ (i >> 1) for i in range(1 << n)] 

sol = Solution()
print(sol.grayCode(2))  
print(sol.grayCode(1))  
