class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True  

        diff_indices = [i for i in range(len(s1)) if s1[i] != s2[i]]

        if len(diff_indices) == 2:
            i, j = diff_indices
            return s1[i] == s2[j] and s1[j] == s2[i]
        
        return False  

Swap_Str = Solution()

print(Swap_Str.areAlmostEqual("bank", "kanb"))
print(Swap_Str.areAlmostEqual("attack", "defend"))
print(Swap_Str.areAlmostEqual("kelb", "kelb"))
