from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(r, c, num):
            box_index = (r // 3) * 3 + (c // 3)
            if num in rows[r] or num in cols[c] or num in boxes[box_index]:
                return False
            return True

        def backtrack():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        for num in map(str, range(1, 10)):
                            if is_valid(r, c, num):
                                board[r][c] = num
                                rows[r].add(num)
                                cols[c].add(num)
                                boxes[(r // 3) * 3 + (c // 3)].add(num)
                                
                                if backtrack():
                                    return True
                                
                                board[r][c] = "."
                                rows[r].remove(num)
                                cols[c].remove(num)
                                boxes[(r // 3) * 3 + (c // 3)].remove(num)
                        return False
            return True
        
        rows, cols, boxes = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + (c // 3)].add(num)
        
        backtrack()
