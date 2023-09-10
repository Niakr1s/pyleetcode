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

        """
        l_int, r_int = int(left), int(right)

        pow = (len(left) // 2 // 2)-1
        pow = 0 if pow < 0 else pow
        half = 10 ** pow
        s = str(half)
        with_middle = len(s) % 2 != 0
        found = 0
        while True:
            s = str(half)
            current_len = len(s)
            s = self.mirror(s, with_middle)

            n = int(s)
            n_pow = n ** 2

            half += 1
            if (len(str(half)) != current_len):
                if with_middle:
                    half //= 10
                with_middle = not with_middle

            if (n_pow < l_int or not self.is_palindrome(s)):
                continue
            if (n_pow > r_int):
                break

            if (self.is_palindrome(str(n_pow))):
                found += 1

        return found

    
    def is_palindrome(self, n: str) -> bool:
        return n == n[::-1]

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
