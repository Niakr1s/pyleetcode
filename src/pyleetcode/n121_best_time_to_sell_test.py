import pytest
from pyleetcode.n121_best_time_to_sell import Solution


@pytest.mark.parametrize(
    ("prices", "expected"),
    (
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
    ),
)
def test(prices, expected):
    assert Solution().maxProfit(prices) == expected
