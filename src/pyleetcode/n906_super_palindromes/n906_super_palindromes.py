from math import sqrt


class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        """
        Constraints:

            1 <= left.length, right.length <= 18
            left and right consist of only digits.
            left and right cannot have leading zeros.
            left is less than or equal to right.

        """
        n = str(int(sqrt(int(left) - 1)))
        found = 0
        while True:
            n = self.next_palindrome(n)
            n2 = str(int(n) ** 2)
            if int(n2) > int(right):
                break
            if self.is_palindrome(n2):
                found += 1

        return found
    
    def is_palindrome(self, n: str) -> bool:
        return n == n[::-1]
    
    def next_palindrome(self, n: str) -> str:
        with_middle = len(n) % 2 == 1
        n_int = int(n)

        mid = len(n) // 2 + len(n) % 2
        left = n[:mid]

        res = n
        while int(res := self.mirror(left, with_middle))  <= n_int:
            was_len = len(left)
            left = str(int(left) + 1)
            if len(left) > was_len:
                if with_middle:
                    left = left[:-1]
                with_middle = not with_middle
        return res

    def mirror(self, n: str, with_middle: bool):
        right = n[:len(n) - 1] if with_middle else n
        return n + right[::-1]
