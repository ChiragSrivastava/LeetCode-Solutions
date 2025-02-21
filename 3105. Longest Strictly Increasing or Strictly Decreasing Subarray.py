class Solution:
    def longestMonotonicSubarray(self, a):
        if not a:
            return 0

        max_length = 1
        inc_length = 1
        dec_length = 1

        for i in range(1, len(a)):
            if a[i] > a[i - 1]:
                inc_length += 1
                dec_length = 1
            elif a[i] < a[i - 1]:
                dec_length += 1
                inc_length = 1
            else:
                inc_length = 1
                dec_length = 1

            max_length = max(max_length, inc_length, dec_length)

        return max_length
SubArray = Solution()
print(SubArray.longestMonotonicSubarray([1, 4, 3, 3, 2]))
print(SubArray.longestMonotonicSubarray([3, 3, 3, 3]))
print(SubArray.longestMonotonicSubarray([3, 2, 1]))
