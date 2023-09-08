import array
import ctypes as ct
import timeit
from functools import cached_property
from typing import List

import shared


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = dict()
        for i, n in enumerate(nums):
            needed = target - n
            if needed in cache:
                return [cache[needed], i]
            cache[n] = i
        raise ValueError("wrong input data")


class Solution_C:
    @cached_property
    def _twoSum_C(self):
        twoSum = ct.CDLL(str(shared.shared_dir / "libn1.so")).twoSum
        twoSum.restype = ct.POINTER(ct.c_int)
        twoSum.argtypes = [
            ct.POINTER(ct.c_int),
            ct.c_int,
            ct.c_int,
            ct.POINTER(ct.c_int),
        ]
        return twoSum

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return_size = ct.c_int(0)
        arr = (ct.c_int * len(nums)).from_buffer(array.array("I", nums))
        res = self._twoSum_C(arr, len(nums), target, ct.pointer(return_size))
        return res[0 : return_size.value]


if __name__ == "__main__":
    nums = list(range(3_000_000))
    target = 500_000

    print(
        "C: \t",
        timeit.timeit("Solution_C().twoSum(nums, target)", globals=globals(), number=1),
    )
    print(
        "PY: \t",
        timeit.timeit("Solution().twoSum(nums, target)", globals=globals(), number=1),
    )
