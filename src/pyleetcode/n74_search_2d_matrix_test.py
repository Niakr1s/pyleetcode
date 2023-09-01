import pytest
from pyleetcode.n74_search_2d_matrix import Solution, Solution2


@pytest.mark.parametrize(
    ("matrix", "target", "expected"),
    (
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 1, True),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 7, True),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 23, True),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 34, True),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 60, True),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 0, False),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 2, False),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 22, False),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 59, False),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 61, False),
    ),
)
def test(matrix, target, expected):
    assert Solution().searchMatrix(matrix, target) == expected
    assert Solution2().searchMatrix(matrix, target) == expected
