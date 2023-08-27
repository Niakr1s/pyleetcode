import pytest
from pyleetcode.n3_longest_substring import Solution


@pytest.mark.parametrize(
    ("input", "expected"),
    (
        ("", 0),
        ("a", 1),
        ("aa", 1),
        ("abcda", 4),
        ("abbcd", 3),
        ("abba", 2),
        ("tmmzuxt", 5),
        ("abcabcbb", 3),
        ("pwwkew", 3),
    ),
)
def test(input, expected):
    assert Solution().lengthOfLongestSubstring(input) == expected
