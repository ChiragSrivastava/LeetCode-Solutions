class Solution:
    def nextPermutation(self, a):
        n = len(a)
        i = n - 2
        
        while i >= 0 and a[i] >= a[i + 1]:
            i -= 1
        
        if i >= 0:
            j = n - 1
            while a[j] <= a[i]:
                j -= 1
            a[i], a[j] = a[j], a[i]
        a[i + 1:] = reversed(a[i + 1:])  

linear_order = Solution()
a = [1, 2, 3]
linear_order.nextPermutation(a)
print(a)
a = [3, 2, 1]
linear_order.nextPermutation(a)
print(a)
a = [1, 1, 5]
linear_order.nextPermutation(a)
print(a)
