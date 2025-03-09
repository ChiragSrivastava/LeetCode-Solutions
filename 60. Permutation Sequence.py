from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = list(range(1, n + 1))
        k -= 1
        result = []
        fact = [1] * n
        for i in range(1, n):
            fact[i] = fact[i - 1] * i
        for i in range(n, 0, -1):
            index = k // fact[i - 1]
            result.append(str(numbers[index]))
            numbers.pop(index)
            k %= fact[i - 1]
        return ''.join(result)
flow_to_heaven = Solution()
print(flow_to_heaven.getPermutation(3, 3))
print(flow_to_heaven.getPermutation(4, 9))
print(flow_to_heaven.getPermutation(3, 1))
