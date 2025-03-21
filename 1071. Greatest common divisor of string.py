import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        gcd_length = math.gcd(len(str1), len(str2))
        return str1[:gcd_length]
value = Solution()
print(value.gcdOfStrings("ABCABC", "ABC"))
print(value.gcdOfStrings("ABABAB", "ABAB"))
print(value.gcdOfStrings("LEET", "CODE")) 
