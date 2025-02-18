from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)
        
        def backtrack():
            nonlocal total
            for ch in count:
                if count[ch] > 0:
                    count[ch] -= 1
                    total += 1
                    backtrack()
                    count[ch] += 1
        
        total = 0
        backtrack()
        return total

sequences = Solution()
print(sequences.numTilePossibilities("AAB"))
print(sequences.numTilePossibilities("AAABBC"))
print(sequences.numTilePossibilities("V"))
