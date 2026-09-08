class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        seen = len(count_t)
        have = 0

        left = 0
        best_len = float('inf')
        best_start = 0

        count_s = {}
        for right in range(len(s)):
            count_s[s[right]] = count_s.get(s[right], 0) + 1

            if s[right] in count_t and count_s[s[right]] == count_t[s[right]]:
                have += 1

            while have == seen:

                if right - left + 1 <  best_len:
                    best_len = right - left + 1
                    best_start = left

                left_char = s[left]
                count_s[left_char] -= 1

                if (left_char in count_t) and count_s[left_char] <  count_t[left_char]:
                    have -= 1
                
                left += 1

        if best_len == float('inf'):
            return ""
        
        return s[best_start: best_start + best_len]
