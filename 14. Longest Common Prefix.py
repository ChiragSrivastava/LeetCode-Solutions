class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        shortest = min(strs, key=len)

        for i in range(len(shortest)):
            if any(string[i] != shortest[i] for string in strs):
                return shortest[:i]
        
        return shortest
