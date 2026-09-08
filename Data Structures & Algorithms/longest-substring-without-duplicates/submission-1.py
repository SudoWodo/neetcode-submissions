class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_window = float('-inf')
        left = 0
        seen = set()

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            window_size = right - left + 1
            max_window = max(max_window, window_size)

        return max_window