from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            return

        m, n = len(matrix), len(matrix[0])
        zero_rows = set()
        zero_cols = set()

        # 1) Find which rows and columns need to be zeroed
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)

        # 2) Set cells to zero if in a marked row or column
        for r in range(m):
            for c in range(n):
                if r in zero_rows or c in zero_cols:
                    matrix[r][c] = 0
