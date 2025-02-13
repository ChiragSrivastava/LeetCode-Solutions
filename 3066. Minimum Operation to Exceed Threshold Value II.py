import heapq

class Solution:
    def minOperations(self, a: list[int], k: int) -> int:
        heapq.heapify(a)
        operations = 0

        while a[0] < k:
            x = heapq.heappop(a)
            y = heapq.heappop(a)
            new_val = min(x, y) * 2 + max(x, y)
            heapq.heappush(a, new_val)
            operations += 1

        return operations
