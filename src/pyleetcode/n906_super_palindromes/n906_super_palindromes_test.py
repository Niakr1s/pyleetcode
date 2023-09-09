import pytest

from .n906_super_palindromes import Solution

test_params = (
    ("left", "right", "expected"),
    (
        ("1", "2", 1),
        ("4", "1000", 4),
        ("1", "11111", 6),
    ),
)


@pytest.mark.parametrize(*test_params)
def test(left, right, expected):
    assert Solution().superpalindromesInRange(left, right) == expected
