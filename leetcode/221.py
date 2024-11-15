from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n_row = len(matrix)
        n_col = len(matrix[0])
        diag_size = [[0] * n_col for _ in range(n_row)]
        row_idx = [[None] * n_col for _ in range(n_row)]
        col_idx = [[None] * n_col for _ in range(n_row)]

        maximal_square = 0
        for r in range(n_row):
            for c in range(n_col):
                if matrix[r][c] == '1':
                    col_idx[r][c] = min(c, col_idx[r][c - 1]) if c != 0 and col_idx[r][c - 1] is not None else c
                    row_idx[r][c] = min(r, row_idx[r - 1][c]) if r != 0 and row_idx[r - 1][c] is not None else r

                    row_size = r - row_idx[r][c] + 1
                    col_size = c - col_idx[r][c] + 1
                    diag_size[r][c] = diag_size[r - 1][c - 1] + 1 if r != 0 and c != 0 else 1
                    valid_size = min(row_size, col_size, diag_size[r][c])
                    diag_size[r][c] = min(diag_size[r][c], valid_size)
                    maximal_square = max(maximal_square, valid_size * valid_size)

        return maximal_square


def main():
    solution = Solution()
    matrix = [["1", "0", "1", "0", "0"],
              ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    assert solution.maximalSquare(matrix) == 4

    matrix = [["0", "1"], ["1", "0"]]
    assert solution.maximalSquare(matrix) == 1

    matrix = [["0"]]
    assert solution.maximalSquare(matrix) == 0

    matrix = [["0", "1", "1", "0", "1"],
              ["1", "1", "0", "1", "0"],
              ["0", "1", "1", "1", "0"],
              ["1", "1", "1", "1", "0"],
              ["1", "1", "1", "1", "1"],
              ["0", "0", "0", "0", "0"]]
    assert solution.maximalSquare(matrix) == 9

    matrix = [["1", "1"],
              ["1", "1"]]
    assert solution.maximalSquare(matrix) == 4


if __name__ == '__main__':
    main()
