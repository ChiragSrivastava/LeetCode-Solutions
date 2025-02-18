from collections import defaultdict

class Solution:
    def tupleSameProduct(self, a):
        total_tuple = defaultdict(int)
        n = len(a)
        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                res = a[i] * a[j]
                total_tuple[res] += 1

        for freq in total_tuple.values():
            if freq > 1:
                count += freq * (freq - 1) * 4

        return count
