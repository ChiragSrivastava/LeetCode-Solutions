class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(num_str, target, start=0, cur_sum=0):
            if start == len(num_str):  
                return cur_sum == target
            for end in range(start + 1, len(num_str) + 1):
                part = int(num_str[start:end])  
                if can_partition(num_str, target, end, cur_sum + part):
                    return True
            return False

        total_punishment = 0

        for i in range(1, n + 1):
            square_str = str(i * i)
            if can_partition(square_str, i):
                total_punishment += i * i

        return total_punishment

Values = Solution()
print(Values.punishmentNumber(10))
print(Values.punishmentNumber(37))
