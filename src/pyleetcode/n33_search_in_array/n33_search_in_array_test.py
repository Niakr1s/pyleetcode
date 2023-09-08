import pytest

from .n33_search_in_array import Solution


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    (
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
    ),
)
def test(nums, target, expected):
    assert Solution().search(nums, target) == expected
