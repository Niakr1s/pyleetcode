class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen: dict[str, int] = {}

        left = 0
        max_len = 0
        for right, ch in enumerate(s):
            if ch in seen and seen[ch] >= left:
                left = seen[ch] + 1
            else:
                max_len = max(max_len, right - left + 1)
            seen[ch] = right
        return max(max_len, len(s) - left)
