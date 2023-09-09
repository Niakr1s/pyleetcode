from math import sqrt


class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        """
        Constraints:

            1 <= left.length, right.length <= 18
            left and right consist of only digits.
            left and right cannot have leading zeros.
            left is less than or equal to right.

        The meaning of the following:

        Let's take a number with 18 digits (maximum possible).
        The square root of a number with 18 digits can have
        a maximum of 9 digits.
        It can only be a palindrome if:
        the left 4 digits are mirrored through the center.
        Therefore, our task is to iterate through palindromes
        within the range from sqrt(left) to 10^5 and check
        if their square is also a palindrome.

        This code beats only 22% of submissions at leetcode,
        so it can be vastly improved, but it works and it's good.

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
        # flag: whether we are folding with middle or not
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

    def mirror(self, s: str, with_middle: bool):
        """
        Mirrors the given string `n` by appending the reverse of its right half.
        
        Parameters:
            n: The string to be mirrored.
            with_middle: Include the middle character of the string in the mirror?
        
        Returns:
            str: The mirrored string.
        """
        right = s[:len(s) - 1] if with_middle else s
        return s + right[::-1]
