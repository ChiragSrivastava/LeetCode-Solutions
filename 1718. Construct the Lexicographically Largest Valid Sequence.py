class Solution:
    def constructDistancedSequence(self, n: int):
        seq = [0] * (2 * n - 1)
        used = set()

        def backtrack(index):
            if index == len(seq):
                return True

            if seq[index] != 0:
                return backtrack(index + 1)

            for num in range(n, 0, -1):
                if num in used:
                    continue
                if num == 1:
                    seq[index] = 1
                    used.add(1)
                    if backtrack(index + 1):
                        return True
                    seq[index] = 0
                    used.remove(1)
                else:
                    if index + num < len(seq) and seq[index + num] == 0:
                        seq[index] = seq[index + num] = num
                        used.add(num)
                        if backtrack(index + 1):
                            return True
                        seq[index] = seq[index + num] = 0
                        used.remove(num)

            return False

        backtrack(0)
        return seq

Valid_Value = Solution()
print(Valid_Value.constructDistancedSequence(3))
print(Valid_Value.constructDistancedSequence(5))
