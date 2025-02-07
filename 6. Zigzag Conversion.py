class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        
        rows = ["" for _ in range(min(numRows, len(s)))]
        curRow = 0
        goingDown = False
        
        for c in s:
            rows[curRow] += c
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            curRow += 1 if goingDown else -1
        
        return "".join(rows)

pattern = Solution()
s = "PAYPALISHIRING"
numRows = 3
print(pattern.convert(s, numRows)) 
numRows = 4
print(pattern.convert(s, numRows)) 
s2 = "A"
numRows = 1
print(pattern.convert(s2, numRows)) 



