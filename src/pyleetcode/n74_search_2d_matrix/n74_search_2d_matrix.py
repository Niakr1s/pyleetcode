from bisect import bisect, bisect_left


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        try:
            row = bisect(matrix, target, key=lambda x: x[0]) - 1
            col = bisect_left(matrix[row], target)
            return matrix[row][col] == target
        except IndexError:
            return False


class Solution2:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        a = _FlattenedMatrix(matrix)
        try:
            idx = bisect_left(a, target)
            return a[idx] == target
        except IndexError:
            return False


class _FlattenedMatrix:
    def __init__(self, matrix: list[list[int]]) -> None:
        self._matrix = matrix

    def __getitem__(self, idx: int) -> int:
        row = idx // len(self._matrix[0])
        col = idx % len(self._matrix[0])
        return self._matrix[row][col]

    def __len__(self) -> int:
        return len(self._matrix) * len(self._matrix[0])
