from bisect import bisect_left, bisect_right


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        result: list[list[int]] = []
        while len(nums) != 0:
            first = nums[0]
            twoSums = self._twoSum(nums[1:], -first)
            result.extend(([first, *twoSum] for twoSum in twoSums))
            nums = nums[bisect_right(nums, first) :]
        return result

    def _twoSum(self, nums: list[int], target: int) -> list[list[int]]:
        result: list[list[int]] = []
        while len(nums) != 0:
            first = nums[0]
            wanted = target - first
            nums = nums[1:]
            found_idx = bisect_left(nums, wanted)
            try:
                if nums[found_idx] == wanted:
                    result.append([first, wanted])
            except IndexError:
                pass
            finally:
                nums = nums[bisect_right(nums, first) : found_idx]
        return result
