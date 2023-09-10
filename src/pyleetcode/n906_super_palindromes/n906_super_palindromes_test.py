
import pytest
from pyleetcode.n906_super_palindromes.n906_super_palindromes_c import Solution_C

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

@pytest.mark.parametrize(*test_params)
def test_C(left, right, expected):
    assert Solution_C().superpalindromesInRange(left, right) == expected