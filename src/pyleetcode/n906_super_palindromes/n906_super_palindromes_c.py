import ctypes as ct
from functools import cached_property

import shared


class Solution_C:
    @cached_property
    def _superpalindromesInRange_c(self):
        fn = ct.CDLL(
            str(shared.shared_dir / "libn906.so")).superpalindromesInRange
        fn.restype = ct.c_int
        fn.argtypes = [ct.c_char_p, ct.c_char_p]
        return fn

    def superpalindromesInRange(self, left, right):
        left = ct.c_char_p(bytes(left, "utf8"))
        right = ct.c_char_p(bytes(right, "utf8"))
        return self._superpalindromesInRange_c(left, right)