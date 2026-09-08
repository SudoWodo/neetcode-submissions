class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        answer = 0
        count = {}

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            max_freq = max(count.values())
            replacements = right - left + 1 - max_freq

            if replacements > k:
                count[s[left]] = count[s[left]] - 1
                left += 1

            answer = max(answer , right - left + 1)
        
        return answer
