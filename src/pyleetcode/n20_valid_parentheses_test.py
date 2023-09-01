import pytest
from pyleetcode.n20_valid_parentheses import Solution


@pytest.mark.parametrize(
    ("input", "expected"),
    (
        (r"", True),
        (r"()", True),
        (r"()[]{}", True),
        (r"(]", False),
        (r"(", False),
        (r")", False),
        (r"{", False),
        (r"}", False),
        (r"[", False),
        (r"]", False),
    ),
)
def test(input, expected):
    assert Solution().isValid(input) == expected
