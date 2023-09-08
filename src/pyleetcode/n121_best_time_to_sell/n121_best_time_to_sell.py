class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 0:
            return 0

        low = high = prices[0]
        profit = 0
        for n in prices:
            if n > high:
                high = n
            elif n < low:
                profit = max(profit, high - low)
                low = high = n
                high = n
        return max(profit, high - low)
