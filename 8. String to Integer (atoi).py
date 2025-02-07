class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        
        sign = 1
        if s[0] in ('-', '+'):
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
        
        result = 0
        for char in s:
            if not char.isdigit():
                break
            result = result * 10 + int(char)
        
        result *= sign
        
        int_min, int_max = -2**31, 2**31 - 1
        if result < int_min:
            return int_min
        if result > int_max:
            return int_max
        
        return result

result_all = Solution()
print(result_all.myAtoi("42"))
print(result_all.myAtoi("   -042"))
print(result_all.myAtoi("1337c0d3"))
print(result_all.myAtoi("0-1"))
print(result_all.myAtoi("words and 987"))
