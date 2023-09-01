import pytest
from pyleetcode.n9_palindrome_number import Solution


@pytest.mark.parametrize(
    ("input", "expected"),
    (
        (121, True),
        (-121, False),
        (10, False),
    ),
)
def test(input, expected):
    assert Solution().isPalindrome(input) == expected
