from bisect import bisect_left


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []
        if len(nums) < 3:
            return result

        nums = sorted(nums)
        for i1, n1 in enumerate(nums[0:-2]):
            if i1 > 0 and nums[i1 - 1] == n1:
                continue

            inner = nums[i1 + 1 :]
            for i2, n2 in enumerate(inner):
                if i2 > 0 and inner[i2 - 1] == n2:
                    continue

                n3 = 0 - n1 - n2
                if _in(inner[i2 + 1 :], n3):
                    result.append([n1, n2, n3])
        return result


def _in(a, x) -> bool:
    i = bisect_left(a, x)
    return i != len(a) and a[i] == x
