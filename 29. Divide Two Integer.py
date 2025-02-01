class Solution:
    def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) != (divisor < 0)

        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        while dividend >= divisor:
            current_divisor = divisor
            multiple = 1
            while dividend >= (current_divisor << 1):
                current_divisor <<= 1
                multiple <<= 1
            dividend -= current_divisor
            quotient += multiple

        quotient = -quotient if negative else quotient

        return max(INT_MIN, min(INT_MAX, quotient))


solution = Solution()

print(solution.divide(10, 3))

print(solution.divide(7, -3))

print(solution.divide(-2147483648, -1))

print(solution.divide(-10, 2))
