from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = dict()
        for i, n in enumerate(nums):
            needed = target - n
            if needed in cache:
                return [cache[needed], i]
            cache[n] = i
        raise ValueError("wrong input data")
