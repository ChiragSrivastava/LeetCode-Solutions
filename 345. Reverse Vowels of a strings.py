class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif s[l] not in vowels:
                l += 1
            else:
                r -= 1
        return "".join(s)
string = Solution()
print(string.reverseVowels("IceCreAm"))
print(string.reverseVowels("leetcode"))
print(string.reverseVowels("hello"))
print(string.reverseVowels("aA"))
