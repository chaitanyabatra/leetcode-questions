from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        board=[["."]*n for _ in range(n)]
        self.solve(0, board, ans, n)
        return ans

    def solve(self, col, board, ans, n):
        if col == n:
            ans.append(["".join(row) for row in board])
            return

        for row in range(n):
            if self.isSafe(row, col, board, n):
                board[row][col] = "Q"
                self.solve(col + 1, board, ans, n)
                board[row][col] = "."

    def isSafe(self, row, col, board, n):
        for i in range(col):
            if board[row][i] == "Q":
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == "Q":
                return False

        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == "Q":
                return False

        return True

