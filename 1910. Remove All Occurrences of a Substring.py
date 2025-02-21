class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part_length = len(part)
        
        for char in s:
            stack.append(char)
            if len(stack) >= part_length and "".join(stack[-part_length:]) == part:
                del stack[-part_length:]
        return "".join(stack)
