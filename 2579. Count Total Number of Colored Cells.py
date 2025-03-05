class Solution:
    def coloredCells(self, n: int) -> int:
        return 2 * n * (n - 1) + 1
Colored_Cells = Solution()
print(Colored_Cells.coloredCells(1))
print(Colored_Cells.coloredCells(2))
print(Colored_Cells.coloredCells(3))
print(Colored_Cells.coloredCells(4))
