class Solution:
    def numberOfAlternatingGroups(self, colors, k):
        n = len(colors)
        count = 0
        valid_windows = 0
        for i in range(k - 1):
            if colors[i] != colors[i + 1]:
                count += 1        
        if count == k - 1:
            valid_windows += 1
        for i in range(1, n):
            if colors[i - 1] != colors[i]:
                count -= 1            
            if colors[(i + k - 2) % n] != colors[(i + k - 1) % n]:  
                count += 1
            if count == k - 1:
                valid_windows += 1
        return valid_windows
colors = Solution()
print(colors.numberOfAlternatingGroups([0,1,0,1,0], 3))
print(colors.numberOfAlternatingGroups([0,1,0,0,1,0,1], 6))
print(colors.numberOfAlternatingGroups([1,1,0,1], 4))
