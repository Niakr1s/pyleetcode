class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        offset = 0
        while True:
            if len(nums) == 1:
                if nums[0] == target:
                    return offset
                else:
                    return -1

            mid = len(nums) // 2
            left, right = nums[:mid], nums[mid:]
            if _is_inside(left, target):
                nums = left
            elif _is_inside(right, target):
                nums = right
                offset += len(left)
            else:
                return -1


def _is_inside(nums: list[int], target: int) -> bool:
    if nums[0] <= nums[-1]:
        return nums[0] <= target <= nums[-1]
    else:
        return target >= nums[0] or target <= nums[-1]
