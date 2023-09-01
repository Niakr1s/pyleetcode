import pytest
from pyleetcode.n15_3sum import Solution


@pytest.mark.parametrize(
    ("nums", "expected"),
    (
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
    ),
)
def test(nums, expected):
    got = Solution().threeSum(nums)
    assert got == expected
