import pytest

from .n1_two_sum import Solution, Solution_C

test_params = (
    ("nums", "target", "expected"),
    (
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ),
)


@pytest.mark.parametrize(*test_params)
def test(nums, target, expected):
    assert Solution().twoSum(nums, target) == expected


@pytest.mark.parametrize(*test_params)
def test_C(nums, target, expected):
    assert Solution_C().twoSum(nums, target) == expected
