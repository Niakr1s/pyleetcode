from bisect import bisect, bisect_left


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        try:
            row = bisect(matrix, target, key=lambda x: x[0]) - 1
            col = bisect_left(matrix[row], target)
            return matrix[row][col] == target
        except IndexError:
            return False
