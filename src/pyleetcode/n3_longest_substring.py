class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = set()
        left = right = max_len = 0
        while len(s) - right != 0 and len(s) - left > max_len:
            if s[right] not in cache:
                cache.add(s[right])
                right += 1
                max_len = max(max_len, len(cache))
            else:
                cache.remove(s[left])
                left += 1

        return max_len
