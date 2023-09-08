class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = list(str(x))
        return s == list(reversed(s))
