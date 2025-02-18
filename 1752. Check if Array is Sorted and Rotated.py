class Solution:
    def check(self, a):
        count = 0
        n = len(a)

        for i in range(n):
            if a[i] > a[(i + 1) % n]:
                count += 1
            if count > 1:
                return False

        return True

checker = Solution()
print(checker.check([3,4,5,1,2]))
print(checker.check([2,1,3,4]))
print(checker.check([1,2,3]))
