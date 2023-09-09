from math import sqrt


class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        left_i = int(left)
        right_i = int(right)

        n = int(sqrt(left_i))
        found = 0
        while (n2 := n * n) <= right_i:
            if n2 >= left_i and self.isPalindrome(n) and self.isPalindrome(n2):
                found += 1
            n += 1

        return found

    @staticmethod
    def isPalindrome(n: int) -> bool:
        return str(n) == str(n)[::-1]