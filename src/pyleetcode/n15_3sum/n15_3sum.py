class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        result: list[list[int]] = []

        for i1, n1 in enumerate(nums[:-2]):
            if i1 > 0 and n1 == nums[i1 - 1]:
                continue

            rem = nums[i1 + 1 :]
            left, right = 0, len(rem) - 1
            while left < right:
                wanted = 0 - n1 - rem[left]
                while right > left and rem[right] > wanted:
                    right -= 1
                if left != right and rem[right] == wanted:
                    result.append([n1, rem[left], rem[right]])

                while left + 1 < len(rem) and rem[left + 1] == rem[left]:
                    left += 1
                left += 1

        return result
