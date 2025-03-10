from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)

        for word in strs:
            sorted_key = tuple(sorted(word))
            anagram_groups[sorted_key].append(word)

        return list(anagram_groups.values())
